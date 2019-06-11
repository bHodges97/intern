#!/bin/bash

FILE="benchmarkdb.csv"

if [ ! -f $FILE ]; then
	touch $FILE
fi

echo -n "`date +%D`" >> $FILE 

./benchmarkmockup.sh | tr -d "[:alpha:] [:blank]" |
while read LINE
do 
	echo -n ", $LINE" >> $FILE
done
echo "" >> $FILE


