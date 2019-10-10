from flask import Flask, request
import json
from SelectDAO import SelectDAO
# from InsertDAO import InsertDAO


app = Flask(__name__)
selector = SelectDAO()

@app.route("/", methods=['POST', 'GET'])
def result():
    return 'post req'


@app.route("/get_companies", methods=['GET'])
def get():
     with open('data/companiess.json') as f:
          data = json.load(f)
          return json.dumps(data)

@app.route("/get_all_user", methods=['GET'])
def get_all():
    selected = selector.select_user('001')
    return json.dumps(selected)

@app.route("/get_companies/", methods=['GET'])
def get_agg_comp():
    user = request.args.get('user')
    selected = selector.select_comp_agg(user)
    return selected

@app.route("/get_charities/", methods=['GET'])
def get_agg_char():
    user = request.args.get('user')
    selected = selector.select_char_agg(user)
    return selected

@app.route("/check_connection", methods=['POST', 'GET'])
def check_connection():
    return "You are connected"

def bootapp():
    app.run(port=5000, host=('127.0.0.1'), debug=True)


if __name__ == '__main__':
     bootapp()

