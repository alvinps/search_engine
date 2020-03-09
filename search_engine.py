import os
import nltk
import math

doc_pool = {}
doc_total = {}

def getidf(token) :
	N = len(doc_names)
	df = 0
	for doc in doc_pool:
		if token in doc:
			df+=1;
	if df == 0 :
		return -1.0
	return math.log( (N/df) ,10)

def gettf(filename , token) :

	if token in doc_pool[filename]:
		return (1 + math.log(doc_pool[filename][token],10)
	else:
		return 0



def getweight(filename , token) :




	return 0




def query( qstring ) :



	return 0;





def main() :

	corpusroot = './presidential_debates'
	nltk.download('stopwords')
	stop_words = set(nltk.corpus.stopwords.words('english'))
	tokenizer = nltk.tokenize.RegexpTokenizer(r'[a-zA-Z]+')
	stemmer = nltk.stem.porter.PorterStemmer()

	for filename in os.listdir(corpusroot):
		file = open(os.path.join(corpusroot, filename), "r", encoding='UTF-8')
		doc_names.append(filename)
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

	print("%15s : %10s \n"% ("Doc Name","Count"))


	for idx in range(0,30):
		print("%15s : %10d \n"% (doc_names[idx],doc_total[idx]))


	print("%.12f" % getidf("hispanic"))




#--------------------------------------------------

if ( __name__ == '__main__' ) :
	main()

#--------------------------------------------------
