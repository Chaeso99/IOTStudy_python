
from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World"

if __name__ == '__main__':
    app.run("0.0.0.0") #어떠한 위치든 가능 