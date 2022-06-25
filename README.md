# tinyarchive
Support Code for DIGHUM 150A's final project.

## Requirements:

Python 3.6+, 
Pip

The rest is in the requirements text. To install the requirements

* clone the archive
* make a virtual environment
    ``` python -m venv <my environment name> ```
* activate the virtual environment, and 
    ``` source <my environment name>/bin/activate ```
* run pip to install the requirements text.
    ``` pip install -r requirements.txt ```

## Other Setup

The project comes with static assets, which you should download from the class webpage and place in the media directory.

## Run the test server

To run the test server in your vm:
* switch to the base directory of the project:
 ``` cd tinyarchive ```
* use the following command.
    ``` python manage.py runserver 0.0.0.0:8000 ```
* view the website on your host machine.
* If you are not running in a vm, you should not need to specify the port or IP address.
