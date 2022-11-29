#!/bin/sh

MAX=110
MIN=40

while true; do
    VALUE=$(($MIN + $RANDOM % $MAX))
    CMD=$(echo localhost:8000/data -d "'"{ \"device_id\": 1, \"decibels\": ' '$VALUE' '}"'" "-H 'Content-Type: application/json'")
    echo "$CMD" | xargs curl
    sleep 5
done