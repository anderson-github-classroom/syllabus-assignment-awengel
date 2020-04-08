#!/bin/bash
for file in `ls *.ipynb`; do
  echo "Testing $file"
  name="${file%.*}"
  pytest ../csc-448-student/tests/test_$name.py
done;

