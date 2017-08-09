#!/bin/bash
# multi file name rename
path=$1
i=1
for file in ${path}/*
do
    if [ ${i} -lt 10 ]; then
        new_name=${path}/0${i}.${file##*.}
    else 
        new_name=${path}/${i}.${file##*.}
    fi
    echo ${new_name}
    mv ${file} ${new_name}
    let i=i+1
done
