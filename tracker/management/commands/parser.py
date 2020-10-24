import requests
import logging


url = "https://api.spacexdata.com/v4/company"


def main():
    logger.debug("Parser started")
    data = requests.get(url).json()
    if type(data) == dict:
        get_keys_and_values_from_dict(d=data)


def get_keys_and_values_from_dict(d: dict):
    for key in d:
        value = d[key]
        print(f"{key}: {value}")
        if type(value) == dict:
            get_keys_and_values_from_dict(d=value)




if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    main()