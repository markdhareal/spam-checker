from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('./model/spam_checker.pkl', 'rb'))

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    text = request.form.get('check_text')

    if not text:
        return render_template('index.html', spam_or_not='No Text')
    
    feature = [text]
    try:
        prediction = model.predict(feature)
        str_predict = str(prediction[0])

        if str_predict == '0':
            result = 'Not Spam'
        else:
            result = 'Spam'
        return render_template('index.html', spam_or_not = f'Prediction: {result}')
    except Exception as e:
        return render_template('index.html', spam_or_not = f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)