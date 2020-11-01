import os
from flask import Flask, Blueprint, request, Response, stream_with_context, render_template
from Sol1_Dropzone import blueprint
import requests
import urllib
from flask import make_response

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix="/blueprint")


@app.route('/')
def create_app():
    return "HEllo WORLD!!"


@app.route('/upload_first')
def upload_1():
    return render_template('upload.html')


@app.route('/upload-page')
def upload_page():
    return render_template('upload_page.html')


@app.route('/upload/<filename>', methods=['POST'])
def upload(filename):
    filename = urllib.parse.unquote(filename)
    print(request.headers)
    bytes_left = int(request.headers.get('content-length'))
    with open(os.path.join('C:/Users/USER/Desktop/bigsizeprob/static/uploads/', filename), 'wb') as upload:
        chunk_size = 5120
        while bytes_left > 0:
            chunk = request.stream.read(chunk_size)
            upload.write(chunk)
            bytes_left -= len(chunk)
        return make_response('Upload Complete', 200)


if __name__ == '__main__':
    app.run()
