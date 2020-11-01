from flask import Flask
from Prob1_dropzone import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix="/blueprint")


@app.route('/')
def create_app():
    return "HEllo WORLD!!"


if __name__ == '__main__':
    app.run()
