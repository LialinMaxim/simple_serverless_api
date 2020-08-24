import json

import requests
from flask import request
from flask_lambda import FlaskLambda

app = FlaskLambda(__name__)


@app.route('/', methods=["POST"])
def load_timer():
    def loader(url):
        try:
            r = requests.get(url)
            return {
                'url': url,
                'status_code': r.status_code,
                'time_load': float(f"{r.elapsed.seconds}.{r.elapsed.microseconds}")
            }
        except BaseException as err:
            print(err)
            return {
                'url': url,
                'status_code': 400,
                'message': 'ConnectionError'
            }

    data = request.json
    urls = data.get('urls', [])

    res = {}
    if isinstance(urls, str):
        res = {"result": [loader(urls)]}
    if isinstance(urls, list):
        res = {"result": [loader(url) for url in urls]}

    return json.dumps(res), 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True)
