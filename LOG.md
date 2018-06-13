# MRB LOG

## 09-05-2018
Created serial communication between pc (python) and arduino (Arduino language).
Got null pointer errors in python.

## 10-05-2018
Null pointer errors gone, they were probably caused by multiple open terminals.
Found a 13v power supply but the fan seems to be to weak.
We will need another fan to compensate for the lack of power.

It's really anoying to find that the provided fan is far too weak for this assignment.

## 15-05-2018
Improved the communication code, it now works good enough.
Got an extra fan and can lift the ball (barely).
We now need to find a way to control the speed of the motor but we have only 1 pin for power.

## 16-05-2016
We can now use pwm by using the SAM3x8e.
The fans need to be lifted from the ground for more airflow (ice cream sticks are too weak). 
The issue is that no solution for this has been provided, this means that we have to "DIY" something.

NOTE: Ask teacher for reimbursement regarding materials.

## 17-05-2016
A platform is created for the fans (thanks Jasper, good thing you had some materials).
We are finally able to lift the ball, to some extend. We are just using a human-PID controller for this.
Only the vision, PID and speaker need to be done now.

## 23-05-2018
Finally managed to write some form of vision.
Let's hope that the PID is at least just as much work, otherwise the balance is nowhere.

## 30-05-2018
Still more work on the vision, it now gives the vertical distance of the detected object.

## 07-06-2018
We can detect every object in the TI-lab but not the ping pong ball, colored paper behind the tube seems to help (or a colored ball).
Fans stopped giving full power. this can not be a power supply issue, as we have an 60W power supply.
Project is gonna fail.

NOTE: We need to contact Marius for new fans.

## 12-06-2018
We found a new ping pong ball, this one is larger and orange. Because of this we have better lift and colored paper behind tube is no longer needed.
This has been more work than it should have been, seeings as this project should have been about PID.

(Jasper zet hier de nieuwe fix voor fans neer.)

## 13-06-2018
We now have a PID controller as well.
This hasn't been more than an hour of work.
Why are we doing a project where we need to spend 40 hours on some vision, while the core of the assignment is the PID controller.
PID parameters were just a matter of trial and error.
Its now possible to set the setpoint using your hand (by computer vision).
