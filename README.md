# Arcade-Retro-Clock
A retro themed clock that plays 9 mini-games.  Written in Python, runs on a Rspberry Pi with the UnicornHD Hat (16x).


[![HD Clock](http://arcaderetroclock.s3.amazonaws.com/images/Clock2.jpg)](https://youtu.be/Ybx1iZNYNkM)
[![HD Clock](http://arcaderetroclock.s3.amazonaws.com/images/Clock1.jpg)](https://youtu.be/Ybx1iZNYNkM)
[![HD Clock](http://arcaderetroclock.s3.amazonaws.com/images/Clock3.jpg)](https://youtu.be/Ybx1iZNYNkM)



Requirements:
Raspberry Pi (supports Zero, 2, 3, 4 and variations)
Python3
Unicorn Hat HD (https://shop.pimoroni.com/products/unicorn-hat-hd)

Setup:
Once you have the pimoroni UnicornHat running on your raspberry pi, download and install the Arcade Retro Clock software.

ArcadeRetroClock.py has input parameters, which were used to control the number of dots appearing, how fast the dots moved, etc.  Run the clock by executing go.sh, which has been pre-configured for a UnicornHat standard, running on a Raspberry Pi A. 

Faster models will cause the display to move too fast to comfortably watch (still fun!) so I suggest modifying the **CPUModifier** parameter.

**Input parameters**
* mainsleep
* flashsleep
* scrollsleep
* mindots 
* maxdots 
* NightModeStart
* NightModeDuration(hours)
* CPUModifier (1 for slow Pi, 5 for Pi2, etc.)
* gamma (used to increase overall brightness -- for Ubercorn display which is somewhat dimmer than the regular small display)
example:  sudo python ArcadeRetroClock.py 0.07 0.07 0.07 20 55 23 7 1

*Note*
The first five parameters are from when the clock was a simple pacman clone.  They will be removed at a later date.  For now just ignore them or use the settings included in the go.sh file.

Here is a description of the games, and what inspired me:

**Outbreak**
 Viruses moving around a petrie dish, consuming the light blue food.  They will replicate, mutate, infect each other, change speed up or down.  I wanted them to clump together and move in the same direction.  Sometimes they shoot off an "explorer" that will infect other colonies.  When a single color virus dominates for 50 moves, a message appears saying "infection cured" or something like that.  The virus number is simply the RGB value of the winning color.

*Note:* This game on the ubercorn is limited to one screen display, but it supports as many as you hook up.  I have several methods.  I have had it on three screens simultaneously so you can see what is going on in other portions of the world.  I did this using http communication between multiple Raspberry Pi installations on the standard unicorn display.  I'll work on that in the future and make a release for much bigger screens.

Inspired by the computer program "Game of Life".

**PacDot**<br>
My first game, very primitive.  Does not use my more advanced objects such as the playfield.  I was learning python as I went.
Inspired by Pacman of course.

**Wormdot**<br>
Just another snake game

**Super Worms**<br>
Started out as a tron lightcycle game.  Morphed into what it is today.  Just something fun to watch.

**DotInvaders**<br>
Space invader clone.  The best part is the time.  You can modify the list of short words as well.  Right now it is some country codes and a few of my friends initials.

**DotZerk**<br>
Green dot is a human trapped in a maze filled with killer robots.  Red dots are robots.  If the human takes too long to kill them, a worse robot shows up.
Game has a lot of bugs, collision detection does not always work.  It is the first game I made with the "playfield" concept where every thing is an object on a playfield.  The program examines each object, not the color of the LED's themselves.

Inspired by the Stern arcade game Berzerk.

**SpaceDot**<br>
Dumb name.  Based on Intellivision Astrosmash.  Ships cross the sky.  Asteroids fall from the sky.  Human ship is protecting the planet.  
If the mother ship gets hit twice it gets angry and starts nuking.

**RallyDot**<br>
This game really got out of hand with complexity.  It started out as a race car game where the dot in the middle is the player, and 8 other race cars try to catch him.  The speed is impressive.  On a raspberry pi 3 it can support 500+ enemy objects.

Each enemy has health and the ability to take damage until they detonate.  The detonation damages nearby enemies which causes a chain reaction.  I am not sure at this point if they are race cars, zombies, or some sort of hybrid.  The maze is fairly straightforward to draw with numbers, you just need to imagine it as you go along.

The game world is larger than the display world, so there is plenty of off screen activity being tracked.  A "camera" shows the current view.  Just like outbreak, this will support multiple screens.

Inspired by RallyX arcade game.


**Orbits (future)**<br>
I decided to get into properly calculating momentum, gravity, inertia, etc.  It is a fairly straighforward concept and I have built solar system simulators before.  I just ran out of steam.  Once I get back into it, this will be amazing.  I have so many ideas but the first one will likely be some sort of pinball game.



** Legacy Code **
This evolved out of a simple pacman clone while I was brand new to Python.  The PacDot code is a mish mash of concepts and is a bit of a mess.  The most recent game added is Outbreak which I believe has much better game architecutre.

There are global variables and parameters sprinkled around that I am still cleaning up.  This is a huge project that I worked on for fun.  I will continue to tidy up the code and isolate the games into their own includable files.

ArcadeFunctions.py is supposed to only have code that is common to all the games, such as the pre-defined sprites, scrolling animations, etc.  It can be used in other projects as well on its own.  I use it in my GPSProbe project.
