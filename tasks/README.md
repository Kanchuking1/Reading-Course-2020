# This folder contains all the solutions to tasks allotted.

## Contributors : 
* Slide 3 : Aditya Bidwai 
* Slide 4 : Advait Kulkarni 
* Slide 5 : Anirudh Panwar
* Slide 6 : Aadhar Sharma
* Slide 7 : Eash Vrudhula
* Slide 8 : Vishal Singh

## Details of files : 

### Note : Make sure you have ROS Melodic installed on your Ubuntu OS. It is a prerequisite to run al the files below

* [roomba.py] is a submission to the task in Slide 4 which demands motion of a turtlebot in an obstacle filled environment similar to that of a roomba or a walker. It uses the lidar data published on the `/scan` topic and publishes corresponding velocity commands on the `/cmd_vel` topic. Follow the following steps to run the simulation : 
1) Launch Turtlebot3 in a house environment : </br>
```roslaunch turtlebot3_gazebo turtlebot3_house.launch```
2) Run the python file which contains the ROS node controlling the Turtebot :  </br>
```python <path_to_roomba.py_file>```

Following are the screenshots and GIF files for the simulation : 


* [controller.py] is a submission for task in Slide 3 which demans motion of a turtlebot in such a way that it moves forward by 5m and turns around by 45 degrees with its positio and orientation logged on a topic or on terminal. The algorithm makes use of the odometry published on the `/odom` topic and velocity commands are published on `/cmd_vel` accordingly. Follow the following steps to run the simulation : 
1) Launch Turtlebot3 in an empty wordl environment : </br>
```roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch```
2) Run the python file which contains the ROS node controlling the Turtebot :  </br>
```python <path_to_controller.py_file>```



