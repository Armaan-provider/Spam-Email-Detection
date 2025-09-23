from flask import Flask, request, render_template
from spam_detection import predict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict_spam():
    if request.method == 'POST':
        message = request.form['input']
        result = predict(message)
        return render_template('index.html', message=message, prediction=result[0])

if __name__ == '__main__':
    app.run(debug=True)
