from flask import Flask, request, jsonify
from models.prediction import LRModel
import numpy as np
app = Flask(__name__)

# instantiate the model
model = LRModel()


@app.route('/api/v1/single_prediction', methods=['POST'])
def single_prediction():
    """
    Get the attributes from the request ( form-data )

    Returns:
        [json]: [response for that request which include the status and the prediction if it exist]
    """
    try:
        temp = float(request.form['temp'])
        atemp = float(request.form['atemp'])
        humidity = float(request.form['humidity'])
        windspeed = float(request.form['windspeed'])
        sample = [temp, atemp, humidity, windspeed]
        prediction = int(model.simple_prediction(sample))

    except:
        response = jsonify({
            'status': '400',
            'message': 'Make sure you do enter the sample correctly'
        })
    else:
        response = jsonify({
            'status': '200',
            'prediction': prediction
        })

    return response


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
