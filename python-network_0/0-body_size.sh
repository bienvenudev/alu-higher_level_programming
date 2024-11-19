#!/bin/bash
# This script takes a URL as an argument and retrieves the size of the response body
curl -s "$1" | wc -c
