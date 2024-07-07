#!/bin/bash
# send delete with URL as first argument
curl -X -s -d "DELETE" "$1"
