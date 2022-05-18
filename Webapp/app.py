#Libraries
from flask import Flask
from flask import render_template
from flask import request
import joblib
from helpers.dummies import gender_dummies

#Creating the app
app=Flask(__name__)

model=joblib.load('models/model.h5')
scaler=joblib.load('models/scaler.h5')

@app.route('/',methods=['GET'])
def home_page():
    return render_template('page1.html')

@app.route('/predict',methods=['GET'])
def predict():
    all_data=request.args
    body_temp=float(all_data['body_temp'])
    heart_rate=float(all_data['heart_rate'])
    exer_dura=float(all_data['exer_dura'])
    weight=float(all_data['weight'])
    height=float(all_data['height'])
    age=int(all_data['age'])
    gender=gender_dummies[all_data['gender']]
    data=[age,height,weight,exer_dura,heart_rate,body_temp]+gender
    scaled_data=scaler.transform([data])
    pred=round(model.predict(scaled_data)[0],2)
    return render_template('page2.html',predicted_calories=pred)
#Running the app
if __name__ == '__main__':
    app.run()