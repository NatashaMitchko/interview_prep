import logging
import requests
import json
from retrying import retry

logging.basicConfig()

def _read_file(filename):
    with open(filename) as f:
        for line in f.lines:
            yield json.load(f.line)


@retry(max_attempts=3)
def _make_request(url, data):
    response = requests.get(url, data=data)
    response.raise_for_status()


def make_requests(url, filename):
    for request in read_file(filename):
        try:
            _make_request(url, json.dumps(request))
        except Exception as e:
            logging.error(f"Failed request: {e}")


###
import responses

@responses.activate
def test_make_request():
    url = "test"
    responses.add(responses.GET, url, status=500)
    _make_request(url, json.dumps({"test": "data"}))
    assert len(responses.calls) == 3
