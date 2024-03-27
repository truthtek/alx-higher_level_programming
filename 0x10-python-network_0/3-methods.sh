#!/bin/bash
# This script displays all HTTP methods accepted by the server at the given URL

methods=$(curl -s -X OPTIONS "$1" -I | grep "Allow:" | cut -d " " -f2-)
echo "$methods"
