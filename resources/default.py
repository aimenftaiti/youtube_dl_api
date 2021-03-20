from flask_restful import Resource
from api.app import api
class DefaultResource(Resource):
    """Handle default route."""
    def get(self):
        """Get request for home page or response."""
        return {
            "status": "success",
            "data": {
                "msg": "Welcome to the Youtube Downloader API"
            }
        }
api.add_resource(DefaultResource, "/api", endpoint="home")