cmake_minimum_required(VERSION 3.12)
project(hikcam)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS -Ofast)
include_directories(${CMAKE_CURRENT_LIST_DIR}/include)

find_package(OpenCV REQUIRED)
find_package(Python3 COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

include_directories(${PYTHON_INCLUDE_DIRS})
set(SOURCES ${CMAKE_CURRENT_LIST_DIR}/hikcam.cpp)

# add_executable(hikcam ${SOURCES})
pybind11_add_module(${CMAKE_PROJECT_NAME} ${SOURCES})

IF (CMAKE_SYSTEM_NAME MATCHES "Linux")
    target_link_libraries(${CMAKE_PROJECT_NAME} PRIVATE $ENV{MVCAM_COMMON_RUNENV}/aarch64/libMvCameraControl.so)
ELSEIF (CMAKE_SYSTEM_NAME MATCHES "Windows")
    target_link_libraries(${CMAKE_PROJECT_NAME} PRIVATE "C:\\Program Files (x86)\\MVS\\Development\\Libraries\\win64\\MvCameraControl.lib")
ELSE ()
    MESSAGE(Error "maybe unsupported platform: ${CMAKE_SYSTEM_NAME}")
ENDIF (CMAKE_SYSTEM_NAME MATCHES "Linux")

target_link_libraries(${CMAKE_PROJECT_NAME} PRIVATE ${OpenCV_LIBS})
target_link_libraries(${CMAKE_PROJECT_NAME} PRIVATE ${PYTHON_LIBRARIES})