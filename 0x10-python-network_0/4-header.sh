#!/bin/bash
# This script sends a GET request with a custom header and displays the body of the response

response=$(curl -s -X GET -H "X-School-User-Id: 98" "$1")
echo "$response"
