from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Hello !'

# app.run(host='0.0.0.0', port=8080)
