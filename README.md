# dockerOrNot
python script to determine if you are in Docker container or not

## Installation

    curl -L https://raw.githubusercontent.com/mfy2a/dockerornot/master/dockerornot.py > /usr/local/bin/dockerornot.py
    chmod +x /usr/local/bin/dockerornot.py

## Usage

    dockerornot
    echo $?
return 100 if in docker - 200 if not

    dockerornot -v

to have an ASCII ART image you can edit the conf part to change ASCII (use images in 'images' folder) and the return code

    notInDocker = {'code': 200, 'image': 'inception.ansi'}
    inDocker = {'code': 100, 'image': 'docker.ansi'}