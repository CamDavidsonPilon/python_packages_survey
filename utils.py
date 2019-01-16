import os

def fetch_from_url_pypi_libraries():
    print("Fetching public PYPI libraries.")
    from lxml import html
    import requests

    response = requests.get("https://pypi.org/simple/")

    tree = html.fromstring(response.content)

    return set(package for package in tree.xpath('//a/text()'))

def load_from_disk_pypi_libraries():
    import pickle
    with open("packages.pickle", 'rb') as f:
        s = pickle.load(f)
    return s



def is_gcp():
    return os.environ.get('GAE_APPLICATION') is not None


