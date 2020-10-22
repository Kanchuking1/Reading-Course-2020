#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist,PoseStamped,Point
import actionlib
from math import atan2,sqrt
import tf

rospy.init_node("world_map",anonymous=True)

listener = tf.TransformListener()
listener.waitForTransform("/odom","/base_footprint",rospy.Time(0),rospy.Duration(5.0))
rate = rospy.Rate(10,0)
while not rospy.is_shutdown():
    try:
        (trans,rot) = listener.lookupTransform("/map", "world",rospy.Time(0))       
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
    rospy.loginfo(trans)
    rate.sleep()
    