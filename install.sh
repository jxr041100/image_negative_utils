#!/bin/bash


mkdir build
cd build
cmake ..
make 

find /home/goddess/workspace/data/ADAS_DEMO/neg -type f -name "*.jpg" > files.txt
./image_negative_util
cd ..

#mkdir result
#mv  -r ./videos/*.jpg ./result/ 

