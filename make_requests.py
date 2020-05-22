import json
import requests
from retrying import retry
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

def generate_requests(filename):
    data = None
    with open(filename) as f:
        data = json.load(f)
        logger.debug("File loaded")
    for i, item in enumerate(data["data"]):
        logging.debug(f"Parsing request {i}/{len(data['data'])}")
        yield item


@retry(stop_max_attempt_number=5)
def make_request(url, data):
    response = requests.get(url, params=data)
    response.raise_for_status()
    logger.info(response.text)
    return response


def call_api(url, filename):
    request_generator = generate_requests(filename)
    for request in request_generator:
        response = make_request(url, request)
    logger.info("doneeeeeee")

if __name__ == "__main__":
    import sys
    call_api(sys.argv[1], sys.argv[2])