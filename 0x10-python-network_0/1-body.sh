#!/bin/bash
# Sends a GET request to a URL without redirection
curl -sL -w "%{http_code}" -o /dev/null "$1"
