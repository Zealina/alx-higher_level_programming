#!/bin/bash
# Return the status code
curl -sw "%{response_code}" "$1"
