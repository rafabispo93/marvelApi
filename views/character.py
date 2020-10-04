from flask import Blueprint
from config import SUFFIXES, DB

import json
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


action_url = "/v1/public/characters"
characters = Blueprint('characters', __name__, url_prefix=action_url)


@characters.route('/', defaults={'char_id': None, 'suffix': None})
@characters.route('/<char_id>', defaults={'suffix': None})
@characters.route('/<char_id>/<suffix>')
def index(char_id, suffix):
    try:
        if char_id:
            res_by_id = DB.get_by_id(int(char_id))
            if suffix in SUFFIXES and res_by_id:
                return res_by_id[suffix], 200
            elif suffix:
                return "Not implemented", 501
            if res_by_id:
                return json.loads(JSONEncoder().encode(res_by_id)), 200
            return "Character not found", 200
        res = DB.get_all()
        if res:
            return JSONEncoder().encode(res), 200
        return "No characters found"
    except Exception as err:
        raise Exception(err)
        return "Internal server error", 500
