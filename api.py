from flask import Flask, request
from flask_cors import CORS
import requests
# from SelectDAO import SelectDAO
# from InsertDAO import InsertDAO


import requests
r = requests.post("http://127.0.0.1:5000/", data={'foo': 'bar'})
print(r.text)



app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def result():
    print(request.form['foo'])
    return 'Received !'

@app.route("/check_connection", methods=['POST', 'GET'])
def check_connection():
    return "You are connected"

def bootapp():
    app.run(port=5000, host=('127.0.0.1'), debug=True)


if __name__ == '__main__':
     bootapp()


