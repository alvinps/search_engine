import os









def main() :
	
	
	

	corpusroot = './presidential_debates'
	for filename in os.listdir(corpusroot):
		file = open(os.path.join(corpusroot, filename), "r", encoding='UTF-8')
		doc = file.read()
		file.close() 
		doc = doc.lower()










		


#--------------------------------------------------

if ( __name__ == '__main__' ) :
	main()

#--------------------------------------------------