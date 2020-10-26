import requests
import logging

#from tracker.models import AboutSpacex


COMPANY_URL = "https://api.spacexdata.com/v4/company"
UPCOMING_LAUNCHES_URL = "https://api.spacexdata.com/v4/launches/upcoming"


def get(url):
    try:
        data = requests.get(url).text
        return data
    except Exception as e:
        logger.error(e)
        return


def get_company_data(url):
    data = get(url)


def get_upcoming_launches_data(url):
    data = get(url)


def main():
    logger.debug("Parser started")
    get_company_data(COMPANY_URL)
    get_upcoming_launches_data(UPCOMING_LAUNCHES_URL)


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    main()