################################################################
################################################################
CMAKE_MINIMUM_REQUIRED (VERSION 2.8)

SET (target "image_negative_util")
PROJECT (${target} CXX)

# define source files
FILE (GLOB src *.h main.cpp)

add_definitions("-std=c++11")

# add current directory to the cmake_module_path for reading the "findiconv.cmake"
LIST(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR} )

#required packages
find_package(OpenCV 2.4 REQUIRED)


INCLUDE_DIRECTORIES (${OPENCV_INCLUDE_DIR})

ADD_EXECUTABLE (${target} ${src})
TARGET_LINK_LIBRARIES (${target} ${OpenCV_LIBS} )

# set linker language
SET_TARGET_PROPERTIES(
	${target} 
	PROPERTIES 
	LINKER_LANGUAGE CXX)

# strange that without this, the project file generated won't compile source files
# on my machine, which seems to me  a bug of cmake.
SET_SOURCE_FILES_PROPERTIES (
	${src} 
	PROPERTIES 
	LANGUAGE CXX)



