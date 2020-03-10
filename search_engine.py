import os
import nltk
import math

doc_pool = {}
doc_total = {}
tf_idf_vec = {}
magnitude = {}
def getidf(token) :
	N = len(doc_pool)
	df = 0
	for doc in doc_pool.keys():
		if token in doc_pool[doc]:
			df+=1
	if df == 0 :
		return -1
	return math.log( (N/df) ,10)



def gettf(filename , token) :

	if token in doc_pool[filename] :
		return (1 + math.log(doc_pool[filename][token],10))
	else :
		return 0

def find_magnitude():

	for file in doc_pool:
		mag = 0
		for key in doc_pool[file]:
			mag += doc_pool[file][key]*doc_pool[file][key]
			mag = math.sqrt(mag)
		magnitude[file] = mag
	return 0


def getweight(filename , token) :
	tf = gettf(filename,token)
	idf = getidf(token)
	if tf == 0:
		return 0
	else:
		magnitude =0;
		for key in doc_pool[filename]:
			magnitude += doc_pool[filename][key]*doc_pool[filename][key]
		magnitude = math.sqrt(magnitude)
		return (tf*idf)/magnitude


def query( qstring ) :



	return 0





def main() :

	corpusroot = './presidential_debates'
	nltk.download('stopwords')
	stop_words = set(nltk.corpus.stopwords.words('english'))
	tokenizer = nltk.tokenize.RegexpTokenizer(r'[a-zA-Z]+')
	stemmer = nltk.stem.porter.PorterStemmer()

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

	find_magnitude()

	print(magnitude)
	tf_idf_vec = doc_pool

	for key in doc_pool['1992-10-15.txt']:
		print()




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





#--------------------------------------------------

if ( __name__ == '__main__' ) :
	main()

#--------------------------------------------------
