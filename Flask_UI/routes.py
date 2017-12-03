from flask import Flask,render_template,request
from forms import submitform
from classifier import productclassifier
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)

app.secret_key = "development-key"

# @app.before_first_request
# def before_first_request():
# 	global vectorizer
# 	fileObject = open('./255_pickle/vectorizer.pickle','rb')
# 	vectorizer= joblib.load(fileObject)
# 	fileObject.close()
# 	global lin_clf
# 	ileObject = open('./255_pickle/lin_clf.pickle','rb')
# 	lin_clf = joblib.load(fileObject)
# 	fileObject.close()



@app.route("/",methods =['GET','POST'])
def index():
	form = submitform()

	if request.method =='POST':
		ab = productclassifier().categoriser(form.querystring.data)
		return render_template('categorized.html',results = ab,form=form)


	elif request.method == "GET":
		return render_template('index.html',form=form)

if __name__=="__main__":
	app.run(debug=True)