import requests
import datetime
from hashlib import md5
from flask import Blueprint
from config import PREFIX, BASE_URL, PRIVATE_KEY, PUBLIC_KEY

action_url = PREFIX+"/characters"
characters = Blueprint('characters', __name__, url_prefix=action_url)


@characters.route('/')
def index():
    try:
        timestamp = str(datetime.datetime.now().timestamp())
        hash_ = timestamp + PRIVATE_KEY + PUBLIC_KEY
        params = {
            "ts": timestamp,
            "apikey": PUBLIC_KEY,
            "hash": md5(hash_.encode()).hexdigest()
        }
        return requests.get(BASE_URL+action_url, params).json()
    except Exception as err:
        raise Exception(err)
