import flask
import os
from flask import request, jsonify, send_file
from pytube import YouTube

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/api/download', methods=['GET'])
def api_url():
    if 'url' in request.args:
        url = request.args['url']
    else:
        return "Error: No url field provided. Please specify an url."

    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download()

    return send_file(stream.download(), as_attachment=True)
app.run()