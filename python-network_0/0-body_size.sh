#!/bin/bash
# This script takes a URL as an argument and retrieves the size of the response body
curl -so /dev/null "$1" -w '%{size_download}\n'
