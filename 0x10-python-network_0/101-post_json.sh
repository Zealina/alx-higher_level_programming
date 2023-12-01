#!/bin/bash
# Post a json file
curl-sX POST -H "Comtent-Type: application/json" -d @"$2" "$1"
