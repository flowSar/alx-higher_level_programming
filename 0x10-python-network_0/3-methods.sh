#!/bin/bash
# print options and methods
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d ' ' -f 2-
