import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
