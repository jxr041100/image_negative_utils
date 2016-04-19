echo off
set ROOT=..\..\
echo ****create the positive vectors based on positive samples*****
opencv_createsamples -info car.dat -w 20 -h 20 -num 175609 -vec vecOpenCVFace15x15.vec




