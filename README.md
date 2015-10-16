# Down to Smash
An application that allows users to create, manage, and find nearby events for impromptu meetups.
HackJam, CalHacks 2.0 2015 Project

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

## Inspiration
The three of us love playing Super Smash Brothers together. Unlike many modern games, it cannot be played online: we must be physically present with each other to play.  It's often difficult to know when we're available, or where we'll be at any given time.  The bandwidth of asking, confirming, and scheduling meetups is often enough to deter us from playing.

It turns out, we're not the only ones who like this game.  In the past two years that we've attended UC Berkeley, interest in Super Smash Brothers has exploded: what was once a small group of friends has now grown into an active and vibrant community.  We now have a corresponding Facebook page with nearly 900 members.

With a growing number of people, we still find ourselves scarce on hardware resources, space, etc.  Organizing meetups is challenging as ever, since everyone is busy.  Sometimes it's scary or embarrassing to post publicly on a Facebook page with so many members, only to not receive a response.  We strove to come up with a solution to this problem.

## What it does

Down to Smash (DTS) is aimed to be a platform where users can create, search, and manage events quickly and efficiently on a whim.  People interested in hosting a gathering can easily create an event that people in the area can view on a visually intuitive map.  Attendees may show interest anonymously as the scour the perimeter, and exchange approval/confirmations with hosts.  Hosts in turn are able to manage their capacity, attendees, and accommodate them as they see fit.  DTS allows people to survey their local area with anonymity, and show interest in multiple events with ease, little commitment, and speed.  The tedious process of meeting up for impulsive events will be no more.  We also see its potential for other activities besides Smash, perhaps such as chess sessions or hangouts.

## How I built it

We first drafted up what we wanted in our application, thinking about the app we wanted -- the app we would use.  We talked about the formats of user interactions, what a user would see, before drawing out the design, models, views, and interactions on pen and paper.  Afterwards, we considered a few web frameworks before deciding upon Django as our full-stack framework: it was a cookie-cutter framework that had the power, tools, support, and documentation for us to learn and work quickly.  First came the creation of models, and tying them to views and templates.  We carefully considered the logic for our application while working with a bare minimum user interface.  From there it was a matter of incorporating basic UI through bootstrap.  

We were set on also utilizing Google Maps, which we had our sights on since the conception of DTS.

## Challenges I ran into

We may have underestimated the difficulties of incorporating certain features, such as the Google Maps API.  The asynchronous programming associated with JavaScript led to major roadblocks in our progress.  Managing the nuances in interactions between models in the database was more challenging than expected.  

## Accomplishments that I'm proud of

Just working through a new framework and being able to build a working application within a few days is also quite the accomplishment, I feel.  We worked efficiently as a team, and ultimately managed to integrate Google Maps successfully, which we were strongly considering dropping because of the difficulties despite our strong desire to use it.  

## What I learned

Always overestimate the time you will need to make even the smallest additions!  Building an app from start to finish is not an easy task to take on.

## What's next for downtosmash

Fixing bugs, mobile port, new features, deployment, Facebook login, lots more!
