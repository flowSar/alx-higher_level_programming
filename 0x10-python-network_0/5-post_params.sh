#!/bin/bash
echo "$1"
curl -s -w "%{size_download}\n" -o /dev/null http://"$1"
