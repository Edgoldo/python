Python3 All in One
==================

Contains several scripts and exercises maked with Python programming interpreted language, each folder save diferents files with sentences, functions, class and methods that help understand how work this language and have some challenges of multiple difficulty levels.

Requirements:
-------------

    Much of this scripts can be executed in Linux terminal, python3 environment or in any python3 console. The basic requirements can be installed by using the following command:

    $ sudo apt-get install python3.5 python3-pip python3.5-dev python3-setuptools 

    To execute the selected script file you must change to correspondant folder in terminal:

    $ cd folder_name

    And then execute:

    $ python3 script_name.py

    To compile any of that files and generate a .pyc file, you can use:

    $ python3 -m py_compile script_name.py

Virtual environment:
--------------------

    To use a virtual environment you can install virtualenv and create that. To install the necesary package you must write in terminal:

    $ sudo apt-get install python3-virtualenv

    And then introduce the next command to create the environment:

    $ virtualenv -p /usr/bin/python3 python_environment

    To activate that virtual environment you must input:

    $ source ~/python_environment/bin/activate

    If all the before steps are correct introduced you will see the name of your environment in the terminal:

    (python_environment) $

Specific Dependencies of Scripts
--------------------------------

    Some of the folders contains README.md files that explains if any file in that folder have other package that it must be installed to run it
