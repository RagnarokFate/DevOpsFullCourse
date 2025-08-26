from flask import Flask
app = Flask(__name__)

@app.route('/hi')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # inner port is already taken so 5000 -> 6000

    # app.run(host='0.0.0.0', port=6000)