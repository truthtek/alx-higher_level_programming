#!/bin/bash
# This script sends a HEAD request to a URL and prints the size of the response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
