from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get symptom data from request
    symptom_data = request.json
    
    # Call predict.py script with symptom data and capture output
    result = subprocess.check_output(['python', 'predict.py', json.dumps(symptom_data)])
    
    # Return the prediction result as JSON
    return jsonify({'predicted_disease': result.decode('utf-8')})

if __name__ == '__main__':
    app.run(debug=True)