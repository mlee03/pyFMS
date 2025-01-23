#!/bin/bash

file_path="./cFMS/libcFMS/.libs/libcFMS.so"

if [ -f "$file_path" ]; then
  echo "File exists"
else
  echo "File does not exist"
fi