#!/bin/bash


# prepare the negative images
python ReadData_neg.py

#prepare the postivie image
python ReadData_pos.py


# ****create the positive vectors based on positive samples*****
opencv_createsamples -info adas.dat -w 20 -h 20 -num 1017 -vec vecADAS20x20.vec


#train
mkdir trained_result
opencv_traincascade -data trained_result -vec vecADAS20x20.vec -bg non_adas.dat -numPos 1000 -numNeg 9000 -numStages 6 -precalcValBufSize 15360 -precalcIdxBufSize 15360 -stageType BOOST -featureType LBP -w 20 -h 20 -bt GAB -minHitRate 0.999 -maxFalseAlarmRate 0.2 -weightTrimRate 0.95 -maxDepth 1 -maxWeakCount 500

