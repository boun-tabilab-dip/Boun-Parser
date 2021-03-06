# coding=utf-8
from flask import Flask, json, g, request, jsonify
import evaluate
import sys
import conllXtostandoff

app = Flask(__name__)

@app.route("/evaluate", methods=["POST"])
def parse_post():
    json_data = json.loads(request.data)
    input_text = json_data["textarea"]
    result = evaluate.parse_plaintext(input_text)
    response = app.response_class(
        response= json.dumps(result),
        status= 200,
        mimetype= 'application/json'
    )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, processes=1, use_reloader=False, port=sys.argv[1])
