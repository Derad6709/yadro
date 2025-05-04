import requests
import logging
import random

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def process_request(url):
    response = requests.get(url)
    logging.info(
        f"Received: {response.status_code} from {url}")
    if 100 <= response.status_code < 400:
        logging.info(
            f"  Status Code: {response.status_code} {response.reason}")
        logging.info(
            f"  Response Body: {response.text if response.text else '[empty]'}"
        )
    elif 400 <= response.status_code < 600:
        raise ConnectionError(
            f"{response.reason} Error ({response.status_code})")
    else:
        logging.warning(
            f"Received unexpected status code: {response.status_code}")


if __name__ == "__main__":
    STATUS_CODES_TO_TEST = [
        200,
        304,
        999,
        random.randint(400, 418),
        random.randint(500, 510),
    ]

    logging.info("--- Starting HTTP Status Code Test Script ---")
    for code in STATUS_CODES_TO_TEST:
        logging.info("---------------------------------------------")
        try:
            process_request(f"https://httpstat.us/{code}")
        except ConnectionError as e:
            logging.error(f"Status: {e}")
    logging.info("-------------- Script Finished --------------")
