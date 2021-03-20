import json
import os
import unittest
from unittest import TestCase

from api.app import create_app

class ResquestTestCase(TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)
    def tearDown(self):
        """
        Will be called after every test
        """
        self.app_context.pop()
    def test_default(self):
        res = self.client.get(
            "/api",
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content_type, "application/json")
        self.assertEqual(res.json["data"]["msg"], "Welcome to the Youtube Downloader API")
    def test_youtube_dl(self):
        res = self.client.get(
            "/api/dl",
            query_string={'url': 'https://www.youtube.com/watch?v=QROfz7Lb7X0'}            
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content_type, "video/mp4")
