import os
import nltk
import math
import collections

#doc_frequency = {}



doc_pool = {}
doc_magnitude = {}
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


	return 0
#--------------------------------------------------

def getweight(filename , token) :
	if token not in tf_idf_vec[filename]:
		return 0
	else:
		return tf_idf_vec[filename][token]
#--------------------------------------------------

def query( qstring ) :
	# qstring = qstring.lower()
	# tokens = tokenizer.tokenize(qstring)
	# qvec = {}
	# N = 0
	# for x in tokens:
	# 	if x not in stop_words:
	# 		N +=1
	# 		stemmed = stemmer.stem(x)
	# 		if stemmed not in qvec:
	# 			qvec[stemmed] = 1
	# 		else:
	# 			qvec[stemmed] += 1
	# mag = 0
	# for x in qvec:
	# 	qvec [x] = 1 + math.log(qvec[x] ,10)
	# 	mag += qvec[x]*qvec[x]
	#
	# mag = math.sqrt(mag)
	# for x in qvec:
	# 	qvec [x] = qvec[x]/mag
	#
	# post_dict = {}
	# for x in qvec:
	# 	post_dict[x] = []
	# 	ls = []
	#
	# 	if x in tf_idf_vec:
	# 		for doc in tf_idf_vec[x]:
	# 			if tf_idf_vec[x][doc] != 0:
	# 				ls.append([doc,tf_idf_vec[x][doc]])
	#
	# 		sorted(ls,key = lambda z:float(z[1]) , reverse=True)
	# 		if len(list) >=10 :
	# 			post_dict[x] = ls[0:10]
	# 		else:
	# 			post_dict[x] = ls
	# sim_score = []
	# for file in doc_pool:
	# 	case1 = True
	# 	for term in qvec:
	# 		all = False
	#
	#
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


	#print("%.12f" % query("health insurance wall street"))



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
