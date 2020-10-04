import unittest
import json
from app import app
from config import SUFFIXES
from views.character import characters


class TestCharacter(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        app.register_blueprint(characters)
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass

    def test_characters(self):
        response = self.app.get("/v1/public/characters", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.data)), 20)

    def test_characters_id(self):
        response = self.app.get("/v1/public/characters/1011334", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["id"], 1011334)
        response = self.app.get("/v1/public/characters/000", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Character not found")

    def test_characters_suffix(self):
        for s in SUFFIXES:
            response = self.app.get("/v1/public/characters/1011334/" + s, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(len(data["items"]), data["returned"])

        response = self.app.get("/v1/public/characters/1011334/test", follow_redirects=True)
        self.assertEqual(response.status_code, 501)
        self.assertEqual(response.data.decode("utf-8"), "Not implemented")


if __name__ == "__main__":
    unittest.main()
