#!/bin/bash
# This script takes a URL as an argument and retrieves the size of the response body
curl -s -I "$1" | grep -i content-length | awk '{print $2}'
