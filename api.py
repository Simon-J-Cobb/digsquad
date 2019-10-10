from flask import Flask, request
from flask_cors import CORS
import requests
# from SelectDAO import SelectDAO
# from InsertDAO import InsertDAO

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST', 'GET'])
def result():
    return 'post req'


@app.route("/check_connection", methods=['POST', 'GET'])
def check_connection():
    return "You are connected"

def bootapp():
    app.run(port=5000, host=('127.0.0.1'), debug=True)


if __name__ == '__main__':
     bootapp()


