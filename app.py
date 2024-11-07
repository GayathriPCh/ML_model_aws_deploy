from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    cgpa = float(request.form.get('cgpa'))
    iq = int(request.form.get('iq'))
    profile_score = int(request.form.get('profile_score'))

    # Make prediction
    result = model.predict(np.array([[cgpa, iq, profile_score]]).reshape(1, 3))

    # Interpret result
    prediction = 'Placed' if result[0] == 1 else 'Not Placed'
    
    return prediction

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)