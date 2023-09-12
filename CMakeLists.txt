cmake_minimum_required(VERSION 3.16)

project(TuiApp VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED true)


include_directories(
        ${PROJECT_SOURCE_DIR}/src
)

file(GLOB all_SRCS "${PROJECT_SOURCE_DIR}/src/*.cpp")


# add_library(src_files src/main.cpp)

# # --- Fetch FTXUI --------------------------------------------------------------
# include(FetchContent)
#
# set(FETCHCONTENT_UPDATES_DISCONNECTED TRUE)
# FetchContent_Declare(ftxui
#   GIT_REPOSITORY https://github.com/ArthurSonzogni/ftxui
#   GIT_TAG v4.0.0
# )
#
# FetchContent_GetProperties(ftxui)
# if(NOT ftxui_POPULATED)
#   FetchContent_Populate(ftxui)
#   add_subdirectory(${ftxui_SOURCE_DIR} ${ftxui_BINARY_DIR} EXCLUDE_FROM_ALL)
# endif()
#
# # ------------------------------------------------------------------------------
# add_executable(ftxui-starter src/main.cpp)
# target_include_directories(ftxui-starter PRIVATE src)
#  
# target_link_libraries(ftxui-starter
#   PRIVATE ftxui::screen
#   PRIVATE ftxui::dom
# )

add_executable(tuiapp ${all_SRCS})

# https://github.com/NEGU93/ForbiddenDesert
