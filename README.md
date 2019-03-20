# Performance Enhancer

_holy moly this repo is a mess_

This is an IoT system designed to be in theatres/small gig venues to allow for performers to trigger
and set lighting to suit their needs. It was made during HtB 2019; winning the ARM prize for most interesting use of ARM hardware and the MLH prize for "Best Hack Using the Dragonboard". Below is a copy of the [Devpost](https://devpost.com/software/performance-enhancer) submission.
## Inspiration

How can we combine all of the things? An overly ambitious hack using new technologies we haven't used before sure! We originally wanted to make Fringe show transition times shorter by abstracting the lighting, sound and images into a block based interface - while we didn't get 80% of it done, the base system is still pretty cool.

## What it does

We can dynamically add new IoT devices to our system such as Låmp and control them through a web app. 

## How we built it

We used React for the frontend and Flask for the server hosted on the Dragonboard. We also have ESP 8266 microcontrollers to control the IoT devices. We wired our own device using a relay to trigger the låmp.

## Challenges we ran into

We don't know how to write React, use microcontrollers or wire låmps so we had difficulty getting things up and running. Therefore we did not manage to build much of the system or construct many IoT devices.

## Accomplishments that we're proud of

Having the ambition to try new technologies, we also drank a lot of Huel.

## What we learned

Over scoping is obvious in hindsight, scope smaller than smaller.

## What's next for Performance Enhancer

Ideally we want to rip it apart and start again but we definitely want to explore IoT more
