# Kideapp helper

## Brief
The project started with kideapp_autoclicker.py which was made with Selenium. Later on made a second version that works with apis, and makes the correct requests. The latter version is more reliable, regarding getting the tickets. Tickets for some student parties are hard to get so I made this program so it's easier for me to get tickets. Not for scalping purposes or public use. The code has been made from scratch, however used internet tools e.g. StackOverflow for help as Selenium was a new library to me when I started this project.

## Future plans
At the moment I use time.sleep()-commands for waiting for certain elements to load, however, I'm planning to switching it to Webdriver.wait(), so I don't have to assume and guess how much time it takes to elements to load. Also probably going to write some simple unittests for the program.

As of 26.12: At the moment there isn't much error handling (e.g faulty bearer token) and not sure if I'm going to implement any. As mentioned the program is only for personal use so the chances of faulty inputs are low.

## Future plan update
I'm not going to update the autoclicker-version any more, as the other one is more reliable and thus better, in my opinion. Some unittests are in progress. Made a simple GUI, even though it wasn't a plan. 

### Used libraries and running the program

Libraries used were PyQt5, requests and Python standard library (time, datetime, sys, json, random, string, unittest). PyQt5 and requests can be installed e.g. from terminal and running command "pip install [library name]". After installing the libraries the project works by running mainwindow.py file.
