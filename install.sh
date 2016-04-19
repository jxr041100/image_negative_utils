#!/bin/bash

rm -rf videos
rm -rf build
rm -rf result

#mkdir videos
#ln -s ~/data/negative/ videos/



mkdir build
cd build
cmake ..
make 

find /home/jeff/data/ -type f -name "*.jpg" > files.txt
./image_negative_util
cd ..

#mkdir result
#mv  -r ./videos/*.jpg ./result/ 

