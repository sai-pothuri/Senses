import os
from flask import Flask, request, jsonify, render_template
import pickle
from werkzeug.utils import secure_filename

app = Flask(__name__)
model = pickle.load(open('model_end.pickle', 'rb'))

def model_predict(img_path, model):
    audio_file = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    x=x/255
    x = np.expand_dims(x, axis=0)
   

   

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    if preds==0:
        preds="The Car IS Audi"
    elif preds==1:
        preds="The Car is Lamborghini"
    else:
        preds="The Car Is Mercedes"
    
    
    return preds

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # final_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)

    # output = round(prediction[0], 2)

    f = request.files['file']

    # Save the file to ./uploads
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(
        basepath, 'uploads', secure_filename(f.filename))
    f.save(file_path)

    # Make prediction
    preds = model_predict(file_path, model)
    result=preds

    return render_template('index.html', prediction_text='Speech recognised is $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)