#!/bin/sh
cut -f 1 chapter2/data/popular-names.txt | sort | uniq -c | sort -nr > chapter2/output/output_sh/output19.txt
# cat chapter2/data/popular-names.txt | cut -f1 | sort | uniq -c | sort -rk1 > chapter2/output/output_sh/output19.txt