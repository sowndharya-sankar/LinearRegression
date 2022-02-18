from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)


@app.route('/home', methods= ['GET','POST'])
@cross_origin()
def home():
    return "Successfull"


if __name__ == '__main__':
    app.run(debug=True)