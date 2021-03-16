'''
    Name: main.py
    Writer: Hoseop Lee, Ainizer
    Rule: Flask app server
    update: 21.02.18
'''

from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__)


# GPT-2 generator.
# Make LoveCraft story
def mk_lovecraft(text, length):
    try:
        data = {
            "text": text,
            "num_samples": 1,
            "length": length
        }

        URL="https://feature-add-torch-serve-gpt-2-server-gkswjdzz.endpoint.ainize.ai/infer/GPT2-large_LoveCraft"
        headers = {
            'Content-Type': 'application/json'
        }
        res = requests.post(URL, headers=headers, data=json.dumps(data))
        
        res = res.json()
        return res

    except Exception as e:
        print('Error occur in script generating!', e)
        return jsonify({'error': e}), 500


##
# Get post request page.
@app.route('/lovecraft', methods=['POST'])
def generate():
    try:
        text = request.form['text']
        length = int(request.form['length'])

        return mk_lovecraft(text, length)

    except Exception as e:
        return jsonify(e), 500


##
# Sever health checking page.
@app.route('/healthz', methods=["GET"])
def health_check():
    return "Health", 200


##
# Main page.
@app.route('/')
def main():
    return render_template('main.html'), 200


if __name__ == '__main__':
    from waitress import serve
    serve(app, port=80, host='0.0.0.0')
