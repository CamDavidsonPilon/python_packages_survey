# -*- coding: utf-8 -*-

"""
Intro
 - links to website
 - small licence  

"""
from __future__ import print_function
from uuid import uuid4
from pprint import pprint
import pkg_resources
import os
import json
from sys import platform, version_info


# Python2/3 have different urllib APIs. 
try:
    from urllib.parse import urlencode
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError, URLError
except ImportError:
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError, URLError

# Python2/3 have different user input APIs
try:
    input = raw_input
except NameError:
    pass


# Are we in the Travis testing environment?
if os.environ.get('TRAVIS'):
    TEST = True
else:
    TEST = False


ENDPOINT = 'https://pip-project-survey.appspot.com/collect'


def python_version():
    return "%d.%d.%d" % (version_info.major, version_info.minor, version_info.micro)


def post_to_api(data, endpoint):
    print("Sending data:")
    pprint(data)
    print()

    if (not TEST) or (input("Confirm sending this to %s (Y/n): " % ENDPOINT) != 'Y'):
        print("Did not send.")
        return

    data = json.dumps(data)
    req =  Request(endpoint, data=data, headers={'Content-Type': 'application/json'})
    req.add_header('Content-Type', 'application/json')
    try:
        resp = urlopen(req)
        print("Sent successfully.")
    except URLError as e:
        print(e)
        print("Connection to endpoint failed. Try again later?")
    except HTTPError:
        print("Server failed. Try again later?")



def generate_uuid():
    uuid = str(uuid4())
    print("You unique identifier is `%s`. Please provide this to us if you wish to delete your data from our database." % uuid)
    return uuid


installed_packages = [(d.project_name, d.version) for d in pkg_resources.working_set]


"""
🔷 Optional to provide, but will help with analysis 🔷

"""

# We'd like to know about why you use Python.
# Provide the closest option in {'science & engineering', 'web development', 'education', 'scripting', 'software development'}.
PRIMARY_USE_OF_PYTHON = None  # a string above

# Are you a contributer to open source software yourself?
CONTRIBUTER_TO_OSS = None  # True, False

# Is this a production system (i.e., not a local / development computer)?
PRODUCTION_SYSTEM = None  # True, False



data = {
    'primary_use': PRIMARY_USE_OF_PYTHON,
    'uuid': generate_uuid(),
    'list_of_installed_packages': installed_packages,
    'test': TEST,
    'platform': platform,
    'python_version': python_version()
}


post_to_api(data, ENDPOINT)




