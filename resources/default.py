from flask_restful import Resource, request
from flask import jsonify, send_file
from pytube import YouTube
from api.app import api

class YoutubeResource(Resource):
    """Handle default route."""
    def get(self):
        """Get request for home page or response."""
        args = request.args
        url = args['url']

        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download()

        return send_file(stream.download(), as_attachment=True)

api.add_resource(YoutubeResource, "/api/dl", endpoint="home")