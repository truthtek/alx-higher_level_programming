#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes

response=$(curl -s "$1")
size=${#response}
echo "$size"
