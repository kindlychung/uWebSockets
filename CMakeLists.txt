
cmake_minimum_required(VERSION 3.8)
set(CMAKE_CXX_STANDARD 17)
set(proj_name uwebsockets)
set(CMAKE_CXX_FLAGS "-g ${CMAKE_CXX_FLAGS}") 
project(${proj_name} CXX)

set(conan_cmake_file "${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
if(EXISTS ${conan_cmake_file})
    include(${conan_cmake_file})
    conan_basic_setup()
endif()
message(CONAN_LIBS ": ${CONAN_LIBS}")

if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release CACHE STRING
    "Choose the type of build, options are: None(CMAKE_CXX_FLAGS or CMAKE_C_FLAGS used) Debug Release RelWithDebInfo MinSizeRel.")
endif ()

add_library(${proj_name}
src/Epoll.cpp
src/Extensions.cpp
src/Group.cpp
src/HTTPSocket.cpp
src/Hub.cpp
src/Networking.cpp
src/Node.cpp
src/Room.cpp
src/Socket.cpp
src/WebSocket.cpp
)
target_link_libraries(${proj_name} ${CONAN_LIBS})

