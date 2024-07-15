#!/bin/bash

# This scrept is created Iam

count=0
num=10
while [ $count -lt 10 ]
do

    echo
    echo $num secomds left to stop this process $1
    echo
    sleep 1

num=`expr $num - 1`
count=`expr $count + 1`
done
echo
echo $1 process is stoped!!!
echo

