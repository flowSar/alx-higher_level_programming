#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
if [ $(curl -s -o /dev/null -w "%{http_code}" http://$1) -eq 200 ]; then curl http://$1; fi
