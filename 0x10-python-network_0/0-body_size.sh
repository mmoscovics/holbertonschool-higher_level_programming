#!/bin/bash
# Takes in a URL, sends a request and displays the size of the body response
curl -s "$@" | wc -c