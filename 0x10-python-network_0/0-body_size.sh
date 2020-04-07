#!/bin/bash
# Takes in a URL, sends a request and displays the size of the body response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f 2
