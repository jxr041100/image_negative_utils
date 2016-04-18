/**
 * @file objectDetection.cpp
 * @author A. Huaman ( based in the classic facedetect.cpp in samples/c )
 * @brief A simplified version of facedetect.cpp, show how to load a cascade classifier and how to find objects (Face + eyes) in a video stream
 */
#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;
using namespace cv;


/**
 * @function main
 */
int main( int argc, const char** argv )
{
  

  Mat frame;
  RNG rng(0xFFFFFFF);
  const char* listname = "../videos/videos.txt"; 
  std::ifstream in(listname);
  string filename; 
  in >> filename;
  while(in.good())
  {
    VideoCapture cap(filename.c_str()); // open the default camera 
    if(!cap.isOpened())  // check if we succeeded
      return -1;

    int frame_number = 0;
    int frame_no = 0;

    //-- 2. Read the video stream
    while( true )
    {      
          cap >> frame;
          frame_no++;

          //if(frame_no>1000) break;

          if(frame_no%10!=0) continue;
          int width = frame.cols;
          int height = frame.rows;
          //extract patches
          for(int patch = 0; patch<10;patch++) 
          {          
             int x = rng.uniform(0,width);
             int y = rng.uniform(0,height);
             int roi_width = width/4;
             int roi_height = width/4;
             if(x+roi_width>=width || y+roi_height>=height) continue;
             Rect roi = Rect(x,y,roi_width,roi_height);
             Mat frame_roi = frame(roi);
             string outfilename = filename.substr(0,filename.length()-1-3) + to_string(frame_number++) + "_out.jpg";
             cout << outfilename << endl;
             imwrite(outfilename,frame_roi);
          }
    }
    in >> filename;
  }

  return 1;
}
