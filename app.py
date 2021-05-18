from flask import Flask, render_template, request, redirect
import requests
import json
import pickle
import numpy as np


app = Flask(__name__)
model = pickle.load(open('models/Final_MinmaxLogisticReg_Model.pkl', 'rb'))
opening_name_freqmap = pickle.load(open('models/opening_name_freqmap.pkl', 'rb'))
openings_list = sorted([var for var in opening_name_freqmap.keys()])
# print(openings_list)


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')
    
@app.route('/predict', methods=['GET' , 'POST'])
def predict():
    return render_template('predict.html', openings_list= openings_list)


@app.route("/result", methods=['GET','POST'])
def result():

    if request.method == 'POST':
        class Chess():
            white_rating = 0
            black_rating = 0
            opening_name = ''
            winner = ''
            prob = ''
            all_prob = 0

        obj = Chess()

        obj.white_rating = int(request.form['White'])
        obj.black_rating = int(request.form['Black'])
        obj.opening_name = request.form['openings']
       
        opening_name = opening_name_freqmap[obj.opening_name]

        sample = [obj.white_rating, obj.black_rating,
                  opening_name, abs(obj.white_rating - obj.black_rating)]
        single_sample = np.array(sample).reshape(1, -1)
        prediction = model.predict(single_sample)
        obj.winner = prediction.item().upper()
        obj.prob = round(max(model.predict_proba(single_sample)[0])*100, 2)
        obj.all_prob = [round(var*100,2) for var in model.predict_proba(single_sample)[0]]
        return render_template('result.html', obj = obj)

    else:
        return render_template('predict.html', openings_list=openings_list)


if __name__ == "__main__":
    app.run(debug=True)
