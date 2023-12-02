#!/bin/bash
# Reveal all the options available for that server
curl -sI "$1" | grep "^Allow:*" | cut -d ' ' -f 2-
