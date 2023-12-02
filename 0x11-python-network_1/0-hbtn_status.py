#!/usr/bin/python3
"""This module contains a function that fetches a documents from a URL"""
import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    print(response.read())
