from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    return request.form['tweet']

if __name__ == '__main__':
    app.run()
