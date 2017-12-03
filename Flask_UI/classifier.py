class productclassifier:
	
	def categoriser(self,querystring1):

		from sklearn.externals import joblib
		import numpy as np
		
		# #if vectorizer==None:
		fileObject = open('./255_pickle/vectorizer.pickle','rb')
		vectorizer= joblib.load(fileObject)
		fileObject.close()

		# #if lin_clf==None:
		fileObject = open('./255_pickle/lin_clf.pickle','rb')
		lin_clf = joblib.load(fileObject)
		fileObject.close()

		test_string = [querystring1]
		test_string = np.array(test_string)
		test_vector = vectorizer.transform(test_string).toarray()

		result = lin_clf.predict(test_vector)[0]
		return result