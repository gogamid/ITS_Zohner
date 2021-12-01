#!/bin/bash
VAR2="NOK\n"
for i in {356015416..356057088}
do
    echo $i
    ./scriptV6.exp $i >> result.txt
done