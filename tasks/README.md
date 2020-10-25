# This folder contains all the solutions to tasks allotted.

## Contributors : 
* Slide 3 : Aditya Bidwai (2018AAPS0388G)
* Slide 4 : Advait Kulkarni 
* Slide 5 : Anirudh Panwar
* Slide 6 : Aadhar Sharma
* Slide 7 : Eash Vrudhula
* Slide 8 : Vishal Singh

## Details of files : 

### Note : Make sure you have ROS Melodic installed on your Ubuntu OS. It is a prerequisite to run all the files below

* [roomba.py](https://github.com/adbidwai/Reading-Course-2020/tree/master/tasks) is a submission to the task in Slide 4 which demands motion of a turtlebot in an obstacle filled environment similar to that of a roomba or a walker. It uses the lidar data published on the `/scan` topic and publishes corresponding velocity commands on the `/cmd_vel` topic. Follow the following steps to run the simulation : 
  1) Launch Turtlebot3 in a house environment : </br>
  ```roslaunch turtlebot3_gazebo turtlebot3_house.launch```
    2) Run the python file which contains the ROS node controlling the Turtlebot : </br>
  ```python <path_to_roomba.py_file>```


* [controller.py](https://github.com/adbidwai/Reading-Course-2020/blob/master/tasks/controller.py) is a submission for task in Slide 3 which demands motion of a turtlebot in such a way that it moves forward by 5m and turns around by 45 degrees with its position and orientation logged on a topic or on terminal. The algorithm makes use of the odometry published on the `/odom` topic and velocity commands are published on `/cmd_vel` accordingly. Follow the following steps to run the simulation : 
  1) Launch Turtlebot3 in an empty world environment : </br>
  ```roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch```
  2) Run the python file which contains the ROS node controlling the Turtebot :  </br>
  ```python <path_to_controller.py_file>```
  
* [world_broadcast.py](https://github.com/adbidwai/Reading-Course-2020/blob/master/tasks/world_broadcast.py) and [world_map.py](https://github.com/adbidwai/Reading-Course-2020/blob/master/tasks/world_map.py) is a submission for task in Slide 6 which asks for a conversion of frame coordiantes. The code makes use of tf library for the transformations Follow the following steps to run the simulation : 
  1) Launch Turtlebot3 in an empty world environment : </br>
  ```roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch```
  2) Run the python file which contains the ROS node controlling the Turtebot :  </br>
  ```python <path_to_world_broadcaster.py_file>```
  3) Run the python file which contains the ROS node controlling the Turtebot :  </br>
  ```python <path_to_world_map.py_file>```
  
  
* [mapping](https://github.com/adbidwai/Reading-Course-2020/tree/master/tasks/mapping) is the solution for Slide 5 which asks for mapping. The results can be seen by launching the launch file inside the `launch` folder of the packages.

* [send_goals](https://github.com/adbidwai/Reading-Course-2020/tree/master/tasks/send_goals) is the solution for Slide 8 which asks for sending goals to the move base client and accordingly the action should be implemented. The results can be seen by launching the launch file inside the `launch` folder of the packages

* [astar.py](https://github.com/adbidwai/Reading-Course-2020/tree/master/tasks/astar.py) is the python code implemented for the visualization and computation of A-star path planning algorithm.


