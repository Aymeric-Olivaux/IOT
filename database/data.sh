#!/bin/sh

MAX=110
MIN=40

while true; do
    VALUE=$(($MIN + $RANDOM % $MAX))
    NUMBER=$((6 + $RANDOM % 17))
    while [ $NUMBER -gt 0 ]; do
        NUMBER=$((NUMBER - 1))
        DELTA=$((-10 + $RANDOM % 10))
        DECIBELS=$(($DELTA + $VALUE))
        CMD=$(echo localhost:8000/data -d "'"{ \"device_id\": 1, \"decibels\": ' '$DECIBELS' '}"'" "-H 'Content-Type: application/json'")
        echo "$CMD" | xargs curl
        sleep 5
    done

done