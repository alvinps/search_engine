import os
import nltk
import math
import collections

#doc_frequency = {}



doc_pool = {}
doc_magnitude = {}
tf_idf_vec = {}

postings_list = {}
nltk.download('stopwords')
stop_words = set(nltk.corpus.stopwords.words('english'))
tokenizer = nltk.tokenize.RegexpTokenizer(r'[a-zA-Z]+')
stemmer = nltk.stem.porter.PorterStemmer()


#--------------------------------------------------


def getidf(token) :
	N = len(doc_pool)
	df = 0
	for doc in doc_pool.keys():
		if token in doc_pool[doc]:
			df+=1
	if df == 0 :
		return -1
	return math.log( (N/df) ,10)

#--------------------------------------------------


def gettf(filename , token) :

	if token in doc_pool[filename] :
		#return 	doc_pool[filename][token] / doc_total[filename]
		return (1 + math.log(doc_pool[filename][token],10))
	else :
		return 0
#--------------------------------------------------


def tfidf_vec_generator():

	for file in doc_pool:
		mag =0
		tf_idf_vec[file] = {}
		for token in doc_pool[file]:
			tf_idf =(getidf(token)*gettf(file,token))
			tf_idf_vec[file][token] = tf_idf
			mag += tf_idf**2
		doc_magnitude[file] = math.sqrt(mag)

	return 0
#--------------------------------------------------

def normalize():

	for file in tf_idf_vec:
		for token in tf_idf_vec[file]:
			tf_idf_vec[file][token] = tf_idf_vec[file][token]/ doc_magnitude[file]
		if token not in postings_list:
			postings_list[token] = {}
			postings_list[token][file] = tf_idf_vec[file][token]

	return 0
#--------------------------------------------------

def getweight(filename , token) :
	if token not in tf_idf_vec[filename]:
		return 0
	else:
		return tf_idf_vec[filename][token]
#--------------------------------------------------

def query( qstring ) :
	qstring = qstring.lower()
	tokens = tokenizer.tokenize(qstring)
	qvec = {}
	tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]

	qtoken_stemmed = collections.Counter(tokens)
	mag = 0
	for term in qtoken_stemmed:
		qtoken_stemmed[term] = 1 + math.log(qtoken_stemmed[term] ,10)
		mag += (1 + math.log(qtoken_stemmed[term] ,10))**2

	magnitude = math.sqrt(mag)

	for term in qtoken_stemmed:
		qtoken_stemmed[term] = qtoken_stemmed[term] / magnitude

	term_in_doc = False
	for term in qtoken_stemmed:
		if term in postings_list:
			term_in_doc = True

	if(not term_in_doc):
		return ("None",0.0)


	return 0




#--------------------------------------------------
def file_reader( corpusroot ) :

	for filename in os.listdir(corpusroot):
		file = open(os.path.join(corpusroot, filename), "r", encoding='UTF-8')
		doc = file.read()
		file.close()
		doc = doc.lower()
		tokens  = tokenizer.tokenize(doc)
		stemmed_tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]
		#doc_frequency += collections.Counter(list(set(stemmed_tokens)))

		token_counter = collections.Counter(stemmed_tokens)
		doc_pool[filename] = token_counter.copy()

		token_counter.clear()


	return 0
#--------------------------------------------------
def test():
	print("getidf:")
	print("%.12f" % getidf("health"))

	print("%.12f" % getidf("agenda"))

	print("%.12f" % getidf("vector"))

	print("%.12f" % getidf("reason"))


	print("%.12f" % getidf("hispan"))


	print("%.12f" % getidf("hispanic"))

	print("getweight:")
	print("%.12f" % getweight("2012-10-03.txt","health"))


	print("%.12f" % getweight("1960-10-21.txt","reason"))


	print("%.12f" % getweight("1976-10-22.txt","agenda"))


	print("%.12f" % getweight("2012-10-16.txt","hispan"))


	print("%.12f" % getweight("2012-10-16.txt","hispanic"))

	print("query:")


	print("(%s, %.12f)" % query("vector entropy"))



	return 0

#--------------------------------------------------



def main() :

	corpusroot = './presidential_debates'

	file_reader( corpusroot )

	tfidf_vec_generator()

	normalize()

	test()







#--------------------------------------------------

if ( __name__ == '__main__' ) :
	main()

#--------------------------------------------------
