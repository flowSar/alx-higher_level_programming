#!/bin/bash
# display size of the body
curl -s -w "%{size_download}\n" -o /dev/null http://"$1"
