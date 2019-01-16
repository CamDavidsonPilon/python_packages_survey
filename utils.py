import os
import hashlib

def fetch_from_url_pypi_libraries():
    print("Fetching public PYPI libraries.")
    from lxml import html
    import requests

    response = requests.get("https://pypi.org/simple/")

    tree = html.fromstring(response.content)

    return set(package for package in tree.xpath('//a/text()'))

def save_pypi_libraries_to_disk():
    import pickle
    s = fetch_from_url_pypi_libraries()
    with open('packages.pickle', 'wb') as f:
        pickle.dump(s, f)

def load_from_disk_pypi_libraries():
    import pickle
    with open("packages.pickle", 'rb') as f:
        s = pickle.load(f)
    return s


def is_gcp():
    return os.environ.get('GAE_APPLICATION') is not None


def md5checksum(s):
    return hashlib.md5(str.encode(s)).hexdigest()

