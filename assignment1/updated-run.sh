#!/bin/bash

docker run -p 5001:5001 -d \
  -v $(pwd):/hostfolder \
  -e GREETING="Spring was earlier." \
  shama7g-assignment1:latest