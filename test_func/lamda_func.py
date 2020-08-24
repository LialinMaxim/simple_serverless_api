import json

import requests


def lambda_handler(event, context):
    def loader(url):
        try:
            r = requests.get(url)
            return {
                'url': url,
                'status_code': r.status_code,
                'time_load': float(f"{r.elapsed.seconds}.{r.elapsed.microseconds}")
            }
        finally:
            return {
                'url': url,
                'status_code': 400,
                'message': 'ConnectionError'
            }

    http_method = event.get('requestContext', {}).get('http', {}).get('method')
    if http_method != 'POST':
        return {
            'statusCode': 400,
            'body': f"method {http_method} not allowed",
        }

    body: json.load(event.get('body', '{}'))
    urls = [v for v in dict(body).items()]

    return {
        'statusCode': 200,
        'body': json.dumps(
            {"result": [loader(url) for url in urls]}
        ),
    }
