#!/bin/bash
# This script sends a JSON POST request with the contents of a file as the request body

url="$1"
file="$2"

if [ -n "$file" ] && [ -f "$file" ]; then
    data=$(cat "$file")
    response=$(curl -s -X POST -H "Content-Type: application/json" -d "$data" "$url")
    echo "$response"
else
    echo "Error: File not found or invalid filename."
fi
