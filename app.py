import time
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Initial distance and limit values
distance = 0
distance_limit = 10  # Set your desired distance limit here

@app.route('/')
def index():
    return render_template('index.html', distance_limit=distance_limit)

@app.route('/get_distance')
def get_distance():
    global distance
    # Simulate getting real distance data
    distance += random.uniform(-1, 1)
    return jsonify({'distance': distance, 'limit': distance_limit})

if __name__ == '__main__':
    app.run(debug=True)
