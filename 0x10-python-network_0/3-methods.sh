#!/bin/bash
# Takes in URL, displays methods the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
