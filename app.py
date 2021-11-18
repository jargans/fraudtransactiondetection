
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app
@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            tramt=float(request.form['ta'])
            tdw=request.form['tdw']
            if (tdw=='Y'):
                tdw=1
            if (tdw=='N'):
                tdw=0
            tdn=request.form['tdn']
            if (tdn=='Y'):
                tdn=1
            if (tdn=='N'):
                tdn=0
            tx1dw=float(request.form['tx1dw'])
            amt1dw=float(request.form['amt1dw'])
            tx7dw=float(request.form['tx7dw'])
            amt7dw=float(request.form['amt7dw'])
            tx30dw=float(request.form['tx30dw'])
            amt30dw=float(request.form['amt30dw'])
            tt1dw=float(request.form['tt1dw'])
            tr1dw=float(request.form['tr1dw'])
            tt7dw=float(request.form['tt7dw'])
            tr7dw=float(request.form['tr7dw'])
            tt30dw=float(request.form['tt30dw'])
            tr30dw=float(request.form['tr30dw'])


            filename = 'final_model.pkl'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[tramt,tdw,tdn,tx1dw,amt1dw,tx7dw,amt7dw,tx30dw,amt30dw,tt1dw,tr1dw,tt7dw,tr7dw,tt30dw,tr30dw]])
            print('prediction is', prediction)
            if prediction[0]==1:
                prediction="Fraud"
            else:
                prediction="not Fraud"
            # showing the prediction results in a UI
            return render_template('results.html',prediction=prediction) 
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')
if __name__ == "__main__":
	app.run(debug=True) # running the app