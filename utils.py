import os

def get_pypi_libraries():
    print("Fetching public PYPI libraries.")
    from lxml import html
    import requests

    response = requests.get("https://pypi.org/simple/")

    tree = html.fromstring(response.content)

    return set(package for package in tree.xpath('//a/text()'))


def is_gcp():
    return os.environ.get('GAE_APPLICATION') is not None


PYPI_LIBS = get_pypi_libraries()
