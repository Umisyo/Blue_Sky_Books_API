# coding: utf-8

from flask import Flask, jsonify
import Sercher as Se

app = Flask(__name__)


@app.route('/')
def hello_world():
    result = Se.All.get_all()

    return jsonify(result)


@app.route('/title=<title>')
def get_title(title=None):
    result = Se.word_search.Searcher( 'title', title )

    return jsonify(result)


@app.route('/first_name=<first_name>', methods=['GET'])
def get_first_name(first_name=None):
    result = Se.word_search.Searcher('first_name', first_name)

    return jsonify(result)


@app.route('/last_name=<last_name>', methods=['GET'])
def get_last_name(last_name=None):
    result = Se.word_search.Searcher( 'last_name', last_name )

    return jsonify(result)


if __name__ == '__main__':
    app.run()
