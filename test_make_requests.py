import requests
import responses
import json
from make_requests import make_request

@responses.activate
def test_call_api():
    test_url = "https://hi.io"
    responses.add(responses.GET, test_url, json={'error': 'not found'}, status=400)
    resp = make_request(test_url, "")
    assert resp.json() == {"error": "not found"}
    assert len(resp.calls) == 1
    assert resp.calls[0].request_url == test_url