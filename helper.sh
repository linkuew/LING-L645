#!/bin/bash

#
# TODO: Fix the code here, I think it's overcalculating
#

# Run this command to see how it works:
# cat [your_conllu_file_here] | awk '/^[^#]/{ print $2, $4, $6 }' | sort | uniq | awk '{ print $1 }' | sort | bash helper.sh

declare -A dict
total=0
dups=0

while read line
do
        # split string here on whitespace
        if [ -z ${dict[$line]} ] ; then
                #echo "assigning value"
                dict[$line]=1
        elif [ ${dict[$line]} -eq 1 ] ; then
                ((dups=dups+1))
        fi
        ((total=total+1))
done < "${1:-/dev/stdin}"

bc --mathlib <<< "(${dups}/${total})"
