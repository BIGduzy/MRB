# MRB LOG

## 09-05-2018
Created serial communication between pc (python) and arduino (Arduino language).
Got null pointer errors in python.

## 10-05-2018
Null pointer errors gone, they were probably caused by multiple open terminals.
Found a 13v power supply but the fan seems to be to weak.

## 15-05-2018
Improved the communication code, it now works good enough.
Got an extra fan and can lift the ball.
We now need to find a way to control  the speed of the motor but we have only 1 pin for power.

## 16-05-2016
We can now use pwm by using the [enter chip name here].
The fans need to be lifted from the ground for more airflow (ice cream sticks are too weak). 

## 17-05-2016
A platform is created for the fans.
We have enough airflow now.
Only the vision, PID and speaker need to be done now.

## 23-05-2018
Wrote the computer vision part.
Can easily see every object on the desk (including hands) but could not test on ping pong ball since i have none at home.

## 30-05-2018
Some minor changes on vision part, it now gives the vertical distance of the detected object.

## 07-06-2018
We can detect every object in the TI-lab but not the ping pong ball, colored paper behind the tube seems to help (or a colored ball).
Fans stopped giving full power.
Project is gonna fail.
We need to contact Marius for new fans.

## 10-06-2018
Colored ball can not be found.
