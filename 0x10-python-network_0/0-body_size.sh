#!/bin/bash
# Bash script that takes in a URL, sends request to URL, displays size
curl -sI 0.0.0.0:5000 | grep 'Content-Length' | cut -d' ' -f2
