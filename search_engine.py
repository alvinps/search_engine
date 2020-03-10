import os
import nltk
import math

doc_pool = {}
doc_total = {}
tf_idf_vec = {}
magnitude = {}
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
		return (1 + math.log(doc_pool[filename][token],10))
	else :
		return 0
#--------------------------------------------------

def find_magnitude(token):

	mag = 0
	for file in doc_pool:
		if token in doc_pool[file]:
			mag += doc_pool[file][token]*doc_pool[file][token]

	return math.sqrt(mag)

#--------------------------------------------------

def tfidf_vec_generator():
	for file in doc_pool:
		tf_idf_vec[file] = {}

	for file in doc_pool:
		for token in doc_pool[file]:
			for x in tf_idf_vec:
				(tf_idf_vec[file])[token] = getweight(file , token)





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
	for x in tokens:
		stemmed = stemmer.stem(x)
		if stemmed not in qvec:
			qvec[stemmed] = 1
		else:
			qvec[stemmed] += 1






	return 0




#--------------------------------------------------
def file_reader( corpusroot ) :

	for filename in os.listdir(corpusroot):
		file = open(os.path.join(corpusroot, filename), "r", encoding='UTF-8')
		doc = file.read()
		file.close()
		doc = doc.lower()
		tokens  = tokenizer.tokenize(doc)
		filtered_dict = {}
		counter = 0
		for word in tokens:
			if word not in stop_words:
				counter+=1
				stemmed = stemmer.stem(word)
				if stemmed in filtered_dict:
					filtered_dict[stemmed]+= 1
				else:
					filtered_dict[stemmed]= 1

		doc_pool[filename] = filtered_dict
		doc_total[filename] = counter


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

	return 0

#--------------------------------------------------



def main() :

	corpusroot = './presidential_debates'

	file_reader( corpusroot )

	tfidf_vec_generator()

	test()







#--------------------------------------------------

if ( __name__ == '__main__' ) :
	main()

#--------------------------------------------------
