#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist 
from nav_msgs.msg.msg import Odometry
from math import pi
from tf import *
global x,y,theta

def callback(msg):
  global x,y,theta
  x = msg.odom.position.position.x
  y = msg.odom.position.position.y
  theta = fromQuaternionToEuler(msg.odom.pose.orientation)[2]

twistMsg = Twist

rospy.init_node("controller_node")
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
sub = rospy.Subscriber('/odom', Odometry, callback)
while (x < 1):
  pub.publish(twistMsg(0.1,0,0,0,0,0))
while(theta < pi/4):
  pub.publish(twistMsg(0.1,0,0,0,0,0.5))
