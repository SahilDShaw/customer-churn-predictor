import flask
import numpy as np
from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route("/")
def index():
	return flask.render_template('index.html')


@app.route("/predict",methods = ['POST'])
def predict():
    if request.method == 'POST':
        jsonData = request.form
        
        a = int(jsonData['gender'])
        b = int(jsonData['seniorCitizen'])
        c = int(jsonData['partner'])
        d = int(jsonData['dependents'])
        e = int(jsonData['tenure'])
        f = int(jsonData['phoneService'])
        g = int(jsonData['multipleLines'])
        h = int(jsonData['internetService'])
        i = int(jsonData['onlineSecurity'])
        j = int(jsonData['onlineBackup'])
        k = int(jsonData['deviceProtection'])
        l = int(jsonData['techSupport'])
        m = int(jsonData['streamingTV'])
        n = int(jsonData['streamingMovies'])
        o = int(jsonData['contract'])
        p = int(jsonData['paperlessBilling'])
        q = int(jsonData['paymentMethod'])
        r = float(jsonData['monthlyCharges'])
        s = float(jsonData['totalCharges'])

        X = np.array([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s]])
        
        pred = loaded_model.predict(X)

        res = 'Yes'
        if(pred[0] == 0): 
            res = 'No'

        # return {'prediction': res}, 200
        return flask.render_template('predict.html', response = res)



if __name__ == '__main__':
    with open('stacking_classifier_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    
        
    app.run(host='0.0.0.0', port=8002, debug=True)