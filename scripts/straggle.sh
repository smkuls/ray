#! /bin/bash

count=1
loop_end=2

while [ $count -le $loop_end ]
do
stress --cpu 1 --timeout 60
echo "Sleeping for 30secs"
sleep 30
(( count++ ))
done

