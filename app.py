#!flask/bin/python
from flask import Flask
from views.character import characters


app = Flask(__name__)

app.register_blueprint(characters)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
