#!/bin/bash

pushd $PWD

#prepare deps
cd deps
if [ -d "smd" ]; then
    cd smd
    git pull
else 
    ./prepare.sh
fi

popd

#build esdm
./configure --prefix=$PWD/install 
cd build
make -j 4
#run tests and benchmark
cmake -E cmake_echo_color
ctest --force-new-ctest-process --no-compress-output -T Test || /bin/true
rm -rf ../generatedJUnitFiles

FILE="benchmarkdb.csv"

if [ ! -f $FILE ]; then
	touch $FILE
else
	rm $FILE
fi

echo "Date, Read, Write" >> $FILE
echo -n "`date +%D`" >> $FILE

./benchmarkmockup.sh | tr -d "[:alpha:] [:blank]" |
while read LINE
do
	echo -n ", $LINE" >> $FILE
done
echo "" >> $FILE:
