# EcoSleep
An energy conservation project which enhances the auto sleep mechanism by including face detection to predict user presence

## About EcoSleep

EcoSleep is an energy saving project implemented using Python, OpenCV and Electron. EcoSleep, using the webcam, detects the presence of a user. In the absence of user, media applications and other selected
applications are suspended and Display is turned off.

## Statistics

### Average Power Consumption - Normal Usage
Normal usage scenario is exhibited when applications such as Games and
Media players are not running. Figure below shows the average running power
consumption of 11.14 Watts.

!(Screenshots/performance_analysis_1.png)


### Average Power Consumption - Running Media Applications
High Power usage scenario is exhibited when applications such as Games and
Media players are running. Figure below shows the average running power consumption
of 15.86 Watts.

!(Screenshots/performance_analysis_5.png)


### Average Power Consumption - Low Power Mode
Low Power usage scenario is exhibited when the user is not present and all the
selected processes are paused and the display unit is turned off. Figure below shows the
average running power consumption of 7.63 Watts.

!(Screenshots/performance_analysis_3.png)


The average power consumption statistics in a given state is as given below.

● Normal Usage - 12 Watts
● Extensive Usage - 15 Watts and greater
● Low Power Mode - 6 Watts

Considering the below usage -
Thirty minutes of inactivity starts the default sleep mechanism. The user is
present for the first ten minutes and absent for the rest.

Power saved = (Normal Consumption - Low Power Consumption) * Low PowerTime
Therefore,
Power saved = (11.14 – 7.63) * (20 * 60) = 4212 Joules.

`Thus, 6 minutes of battery life would have been saved.`
