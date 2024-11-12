from flask import Flask, jsonify, render_template
import requests
import json

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    data = {
        "suhumax": 36,
        "suhumin": 11,
        "suhurata": 28.35,
        "nilai_suhu_max_humid_max": [
            {
                "idx": 181,
                "suhu": 36,
                "humid": 35,
                "kecerahan": 25,
                "timestamp": "2010-09-18 07:23:49"
            },
            {
                "idx": 226,
                "suhu": 36,
                "humid": 36,
                "kecerahan": 27,
                "timestamp": "2011-05-02 12:29:34"
            }
        ],
        "month_year_max": [
            {
                "month_year": "9-2010"
            },
            {
                "month_year": "5-2011"
            }
        ]
    }
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    return jsonify(data)

@app.route('/')
def index():
    response = requests.get('http://localhost:5000/data')
    data = response.json()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
