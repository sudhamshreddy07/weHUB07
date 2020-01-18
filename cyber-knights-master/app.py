import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html', status='Safe')


# @app.route('/predict/', methods=['POST'])
# def predict():
#     # inputs = []
#     # for input in request.form.values():
#     #     input.append(input)
#     #
#     # inputs = [np.array(inputs)]
#     # prediction = model.predict(inputs)
#
#     return render_template('smart_guide.html', abcde  ='{}'.format('Cyber Knights'))


if __name__ == "__main__":
    app.run(debug=True)