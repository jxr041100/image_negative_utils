#!/bin/bash


# prepare the negative images
python ReadData_neg.py

#prepare the postivie image
python ReadData_pos.py


# ****create the positive vectors based on positive samples*****
opencv_createsamples -info car.dat -w 20 -h 20 -num 175609 -vec vecCar20x20.vec


#train
mkdir trained_result
opencv_traincascade -data trained_result -vec vecCar20x20.vec -bg non_car.dat -numPos 50000 -numNeg 1000000 -numStages 14 -precalcValBufSize 15360 -precalcIdxBufSize 15360 -stageType BOOST -featureType LBP -w 20 -h 20 -bt GAB -minHitRate 0.999 -maxFalseAlarmRate 0.2 -weightTrimRate 0.95 -maxDepth 1 -maxWeakCount 500

