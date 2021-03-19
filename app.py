import flask
import os
from flask import request, jsonify, send_file
from pytube import YouTube

app = flask.Flask("Youtube Downloader")

@app.route('/youtube/api', methods=['GET'])
def home():
    return '''<h1>Faut mettre un lien en fait
    </h1>'''

@app.route('/youtube/api/download', methods=['GET'])
def api_url():
    if 'url' in request.args:
        url = request.args['url']
    else:
        return "Error: No url field provided. Please specify an url."

    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download()

    return send_file(stream.download(), as_attachment=True)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=os.getenv('PORT'))