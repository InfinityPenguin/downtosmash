# Down to Smash
An application that allows users to create, manage, and find nearby events for impromptu meetups.
HackJam, CalHacks 2.0 2015 Project
View the submission at http://devpost.com/software/downtosmash

Installation for devs
==============
0. Install Python 3. Modern versions of Python will come with `pip`; see http://pip.readthedocs.org/en/stable/installing/ for more information
1. Run `pip install virtualenv`.  This is a tool that sandboxes your environment to keep dependencies consistent.  More info at http://docs.python-guide.org/en/latest/dev/virtualenvs/
2. Install `virtualenvwrapper' to make using `virtualenv` easier.  It also places all your virtual environments in one place: 
	- `pip install virtualenv`
	Append these two lines to the end of your .bashrc:
	- `export WORKON_HOME=~/envs`
	- `source /usr/local/bin/virtualenvwrapper.sh`
3. Create a new virtual environment: `mkvirtualenv dts`
4. and enter it: `workon dts`
5. Clone this git repo
6. Install dependencies: `pip install -r requirements.txt`
7. To exit the virtualenv, run `deactivate`
