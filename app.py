# coding: utf-8

from flask import Flask, jsonify
import Sercher as S

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/title=<title>')
def get_title(title=None):
    result = S.word_serch.Sercher(True, 'title', title)

    return result


@app.route('/first_name=<first_name>')
def get_first_name(first_name=None):
    result = S.word_serch.Sercher(True, 'first_name', first_name)

    return result


@app.route('/last_name=<last_name>')
def get_last_name(last_name=None):
    result = S.word_serch.Sercher()


if __name__ == '__main__':
    app.run()
