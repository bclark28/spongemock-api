import random

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/spongemock', methods=["GET"])
def mockText():
    if validate_query(request):
        string = request.args.get('text')
        chars = [x for x in string.lower()]
        mocked_string = []

        for char in chars:
            if random.randint(0, 1) > 0:
                mocked_string.append(char.upper())
            else:
                mocked_string.append(char)

        return jsonify({
            "error": None,
            "mockedText": "".join(mocked_string)
        }), 200
    else:
        return jsonify(invalid_query()), 400


def validate_query(request_data):
    if request_data.args.get('text') is None:
        return False

    if type(request_data.args.get('text')) is not str:
        return False

    return True


def invalid_query():
    return {
        "error": "query is not valid",
        "mockedText": None
    }


if __name__ == '__main__':
    app.run(port=5000)
