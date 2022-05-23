import os
from flask import Flask, request, jsonify, render_template
import pickle
from werkzeug.utils import secure_filename
from speech_recognition import speech_api

app = Flask(__name__)
# model = pickle.load(open('model_end.pickle', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/predict',methods=['POST'])
# def predict():
#     '''
#     For rendering results on HTML GUI
#     '''

#     f = request.files['file']

#     # Save the file to ./uploads
#     basepath = os.path.dirname(__file__)
#     file_path = os.path.join(
#         basepath, 'uploads', secure_filename(f.filename))
#     f.save(file_path)

#     # Make prediction
#     preds = model_predict(file_path, model)
#     result=preds

#     return render_template('index.html', prediction_text='Speech recognised is $ {}'.format(output))

@app.route('/speech_recognition',methods=['POST'])
def speech_recognition():
    '''
    For rendering results on HTML GUI
    '''

    return render_template('speech.html')

def speech():

    return render_template('test.html')

@app.route('/speech_recognition_predict',methods=['POST'])
def speech_recognition_predict():
    f = request.files['file']
    # Save the file to ./uploads
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(
        basepath, 'uploads', secure_filename(f.filename))
    f.save(file_path)

    text = speech_api(file_path)
    return render_template('test.html', prediction_text=text)



if __name__ == "__main__":
    app.run(debug=True)