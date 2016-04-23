# image_negative_utils

######### current program is written by Jianfeng Ren, which will generate more negative samples for training.

1. firstly download *.mp4 format video into ~/data/download
2. go to install.sh to change the 
   ln -s ~/data/download videos/

3. then run ./install.sh

4. finally the converted patches are in result folder.



##################### in the object_detect_train folder, it will 
call prepare the positive and negative samples for training.
then call opencv_train_cascade to train the detector. 
