from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/')
def get_time():
    return jsonify({"time": int(time.time())})

if __name__ == '__main__':
    app.run(debug=True)
