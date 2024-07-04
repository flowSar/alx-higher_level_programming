#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -s -w "%{http_code}" -o response.txt http://$1 | awk 'NR==1 && $0=="200" { system("cat response.txt") }'
