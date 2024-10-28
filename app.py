from flask import Flask, request, render_template
import numpy as np
import pickle
import sklearn
print(sklearn.__version__)
#loading models
model = pickle.load(open('model.pkl', 'rb'))
preprocessor = pickle.load(open('preprocesser.pkl', 'rb'))

#flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Crop.html')
    
@app.route("/predict",methods=['POST'])

# Area, Annual_Rainfall, Fertilizer, Pesticide, Production, Crop_Year, State, Crop, Season

def predict():
    if request.method == 'POST':
        Area = request.form['Area']
        Annual_Rainfall = request.form['Annual_Rainfall']
        Fertilizer = request.form['Fertilizer']
        Pesticide = request.form['Pesticide']
        Production  = request.form['Production']
        Crop_Year = request.form['Year']
        State  = request.form['State']
        Crop  = request.form['Crop']
        Season  = request.form['Season']

        features = np.array([[Area, Annual_Rainfall, Fertilizer, Pesticide, Production, Crop_Year, State, Crop, Season]], dtype=object)
        transformed_features = preprocessor.transform(features)
        prediction = model.predict(transformed_features).reshape(1, -1)

        return render_template('Crop.html', prediction = prediction[0][0])

if __name__=="__main__":
    app.run(debug=True)