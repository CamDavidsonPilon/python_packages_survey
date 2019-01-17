# -*- coding: utf-8 -*-
from __future__ import print_function

# 🔷 Optional answers to provide, but will help with analysis 🔷

# We'd like to know about why you use Python most often.
# Provide the closest option in:
#  'science & engineering', 'web development', 'education',
#  'scripting', 'software development', 'other'
PRIMARY_USE_OF_PYTHON = None  # a string above

# Have you ever contributed a lot of time to an open source project?
CONTRIBUTER_TO_OSS = None  # True, False

# Is this running on a production system 
# (i.e., not a local / development / personal computer)?
PRODUCTION_SYSTEM = None  # True, False

# How many years have you been using Python?
YEARS_USING_PYTHON = None  # float

# Approximately, how many days per month do you work with Python?
PYTHON_MONHTLY_USAGE = None  # integer <= 30

#############################################################

from uuid import uuid4
from pprint import pprint
import pkg_resources
from string import printable
import os
import json
from sys import platform, version_info
try:
    # Python2/3 have different urllib APIs.
    from urllib.parse import urlencode
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError, URLError
except ImportError:
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError, URLError
try:
    # Python2/3 have different user input APIs
    input = raw_input
except NameError:
    pass

TEST = True if os.environ.get("TRAVIS") else False
HIDE_EMOJI = True if (os.name == "nt" or TEST) else False
ENDPOINT = "https://python-packages-survey.com/collect"


def python_version():
    try:
        # python 2.6 does this differently...
        return "%d.%d.%d" % (version_info.major, version_info.minor, version_info.micro)
    except:
        return "%d.%d.%d" % (version_info[0], version_info[1], version_info[2])


def post_to_api(data, endpoint):
    console_print("Sending the following data:", end='\n\n')
    pprint(data)
    print()
    console_print("✨ All private libraries are filtered out before hitting the database ✨", end='\n\n')
    console_print("Your unique identifier is `%s`." % data['uuid'])
    console_print("""Please provide this to us if you wish to delete your data from our database.""", end='\n\n')
    if not TEST:
        if input("🔷 Please confirm sending this data to %s (Y/n): " % ENDPOINT) != "Y":
            console_print("Aborted sending.")
            return
    print()
    data = json.dumps(data)
    if python_version() >= "3":
        # converts to bytes
        data = str.encode(data)

    req = Request(endpoint, data=data, headers={"Content-Type": "application/json"})
    try:
        resp = urlopen(req)
        console_print("🎉 Sent successfully. Thank you for participating in the survey!")
    except URLError as e:
        console_print("Possible data validation failure or connection to endpoint failed. Try again later?")
    except HTTPError:
        console_print("Server failed. Try again later?")


def generate_uuid():
    uuid = str(uuid4())
    return uuid

def console_print(text, *args, **kwargs):
    """Given a string, console_prints to console by first stripping emoji if applicable."""
    if HIDE_EMOJI:
        clean_text = ''.join(char for char in text if char in printable)
        print(clean_text.strip(), *args, **kwargs)
    else:
        print(text, *args, **kwargs)


data = {
    "primary_use": PRIMARY_USE_OF_PYTHON,
    "uuid": generate_uuid(),
    "list_of_installed_packages": [(d.project_name, d.version) for d in pkg_resources.working_set],
    "test": TEST,
    "platform": platform,
    "python_version": python_version(),
    "years_using_python": YEARS_USING_PYTHON,
    "python_monthly_usage": PYTHON_MONHTLY_USAGE,
}

post_to_api(data, ENDPOINT)
