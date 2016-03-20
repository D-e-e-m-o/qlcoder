#!/bin/bash

for i in `seq 365000`;do
    mydate=$(date -d 19900101+${i}day +%Y%m%d)
    mydatemd5=$(echo -n ${mydate} | md5sum | cut -d ' ' -f1)
    #echo $mydatemd5
    if [[ $mydatemd5 == '7e38890b870934b126f66857ed6b57b9' ]];
	then
        echo $mydate;
        break;
    fi
done