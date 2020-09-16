#!/bin/bash

python /app/do.py

counter=0
while read line
do
    if  [[ "$counter" -eq 0 ]]; then
        echo -e "\n\n>> modified: $line"
        file="$(echo $line | awk '{print $NF}')"
        echo -e ">> Script OUTPUT >>\n"
        python /app/do.py
        counter=1
    else
        counter=0
    fi
done < <(inotifywait -mr -e modify "/app/")