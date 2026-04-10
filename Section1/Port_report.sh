#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <IP>"
  exit 1
fi

IP=$1
DATE=$(date +%F)
FILE="scan_${IP}_${DATE}.txt"

PORTS=(21 22 80 443 3306)
OPEN_COUNT=0

for PORT in ${PORTS[@]}
do
  timeout 1 bash -c "echo >/dev/tcp/$IP/$PORT" 2>/dev/null &&
  echo "Port $PORT: OPEN" | tee -a $FILE && ((OPEN_COUNT++)) ||
  echo "Port $PORT: CLOSED" >> $FILE
done

echo "Total open ports: $OPEN_COUNT"