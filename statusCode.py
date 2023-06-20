import requests
from requests.exceptions import ConnectionError


def status_checker(domain):
    try:
        request = requests.get(domain)
    except ConnectionError:
        err = "unreachable"
        return domain, err
    else:
        status_code = request.status_code
        return domain, status_code
