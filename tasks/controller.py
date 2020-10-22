#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist 
from nav_msgs.msg.msg import Odometry 

def callback(msg):


rospy.init_node("controller_node")
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
sub = rospy.Subscriber('/odom', Odometry, callback)
while not rospy.is_shutdown
