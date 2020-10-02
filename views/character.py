import requests
import datetime
from hashlib import md5
from flask import Blueprint
from config import PREFIX, BASE_URL, PRIVATE_KEY, PUBLIC_KEY, SUFFIXES

action_url = PREFIX+"/characters"
characters = Blueprint('characters', __name__, url_prefix=action_url)


@characters.route('/', defaults={'char_id': None, 'suffix': None})
@characters.route('/<char_id>', defaults={'suffix': None})
@characters.route('/<char_id>/<suffix>')
def index(char_id, suffix):
    try:
        timestamp = str(datetime.datetime.now().timestamp())
        hash_ = timestamp + PRIVATE_KEY + PUBLIC_KEY
        params = {
            "ts": timestamp,
            "apikey": PUBLIC_KEY,
            "hash": md5(hash_.encode()).hexdigest()
        }
        url = BASE_URL+action_url

        if char_id:
            url = url + "/"+char_id
            if suffix in SUFFIXES:
                url = url + "/"+suffix
            elif suffix:
                return "Not implemented", 501

        request = requests.get(url, params)
        if request.status_code == 200:
            return request.json()["data"], request.status_code
        return request.json(), request.status_code

    except Exception as err:
        raise Exception(err)
        return "Internal server error", 500
