#!/bin/bash
# This script takes a URL as an argument and retrieves the size of the response body
curl -sI "$1" | grep -i content-Length | awk '{print $2}'
