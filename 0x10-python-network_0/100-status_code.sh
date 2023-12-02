#!/bin/bash
# Return the status code
curl -s -o /dev/null -w "%{response_code}" "$1"
