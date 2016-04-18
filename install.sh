#!/bin/bash

rm -rf videos
rm -rf build
rm -rf result

mkdir videos
ln -s ~/Jeff/data/download/*.mp4 videos/

mkdir build
cd build
cmake ..
make 

ls ../videos/*.mp4 > ../videos/videos.txt
./image_negative_util
cd ..

mkdir result
mv ./videos/*.jpg ./result/ 

