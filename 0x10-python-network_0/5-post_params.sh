#!/bin/bash
# This script sends a POST request with parameters and displays the body of the response

response=$(curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1")
echo "$response"
