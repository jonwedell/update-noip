#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function

import requests
import ipgetter
import random

try:
    from settings import USERNAME, PASSWORD, HOSTNAME
except:
    HOSTNAME = ""  # noip.com hostname
    USERNAME = ""  # noip.com username
    PASSWORD = ""  # noip.com password

_new_ = ipgetter.myip()
_url_ = "https://dynupdate.no-ip.com/nic/update?hostname={hostname}&myip={ip}"

# Update current public ip
_url_called_ = _url_.format(hostname=HOSTNAME, ip=_new_)
r = requests.get(_url_called_, auth=(USERNAME, PASSWORD))

if r.status_code != 200:
    print("Error during IP update (%s): %s" % (str(r.status_code), r.content))


