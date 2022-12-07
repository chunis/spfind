#!/bin/sh

# find all files in $1 and saved at file '$db'; without $1, find files in pwd 
#
# Chunis Deng (chunchengfh@gmail.com)
# ver: 0.1, 2011/06/27

db="/tmp/myspfind.db"
path=$1

if [ "$path" = "" ]; then
	path=`pwd`
fi

echo $path | grep -s '^/'
[ $? = 0 ] || path=`pwd`/$path
echo $path

rm -f $db
find $path -type f > $db
