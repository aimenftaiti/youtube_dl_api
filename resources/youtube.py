from flask_restful import Resource, request
from flask import jsonify, send_file
from pytube import YouTube
from api.app import api

class YoutubeDownloadResource(Resource):
    """Handle youtube downloader route."""
    def get(self):
        args = request.args
        url = args['url']

        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download()

        return send_file(stream.download(), as_attachment=True)


api.add_resource(YoutubeDownloadResource, "/api/dl", endpoint="youtube_dl")