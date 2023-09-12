import logging
import os
import subprocess
import sys

BUILD_DIR = "build"


def run_cmake(url):
    try:
        os.chdir(url)
        subprocess.Popen("cmake ..", shell=True)
    except Exception as e:
        logging.error("Something went wrong!")
        print(e)
        sys.exit(1)

def main():
    url = os.path.join(os.getcwd(), BUILD_DIR)
    if not os.path.exists(url) or os.path.isdir(url):
        os.mkdir(BUILD_DIR)
        build_dir_path = url
    else:
        build_dir_path = os.path.join(os.getcwd(), BUILD_DIR)
    run_cmake(build_dir_path) 



if __name__ == "__main__":
    main()
