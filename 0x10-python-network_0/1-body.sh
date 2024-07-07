#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -s -L -o /dev/null -w "%{html_body}" "$1" | grep -q "^200 " && cat || true
