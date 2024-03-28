#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me and displays the response body

response=$(curl -s -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me)

printf '%s\n' "$response"
