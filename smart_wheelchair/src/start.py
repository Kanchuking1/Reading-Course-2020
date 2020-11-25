#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Image
from move_robot import MoveRobot

lidar_flag = 0
threshold = 0.8 

def lidar_callback(msgs):
	global lidar_flag
	global threshold
	print '-------------------------------------------'
	print 'Range data at 0 deg:   {}'.format(msgs.ranges[0])
	print 'Range data at 15 deg:  {}'.format(msgs.ranges[15])
	print 'Range data at 345 deg: {}'.format(msgs.ranges[345])
	print '-------------------------------------------'
	if msgs.ranges[0]>threshold and msgs.ranges[15]>threshold and msgs.ranges[345]>threshold:
		lidar_flag = 0 #safe
	else:
		lidar_flag = 1 #fatal



class LineFollower(object):
	def __init__(self):

		self.bridge_object = CvBridge()
		self.image_sub = rospy.Subscriber("/kinect/rgb/image_raw",Image,self.camera_callback)
		#self.lidar_sub = rospy.Subscriber("/scan", LaserScan, self.lidar_callback)
		self.moverobot_object = MoveRobot()
		self.threshold = 0.8

	def camera_callback(self,data):
		global lidar_flag
		try:
			# We select bgr8 because its the OpneCV encoding by default
			cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
		except CvBridgeError as e:
			print(e)

		
		# Crop the image
		height, width, channels = cv_image.shape
		descentre = 220
		rows_to_watch = 20
		crop_img = cv_image[(height)/2+descentre:(height)/2+(descentre+rows_to_watch)][1:width]

		# Convert from RGB to HSV
		hsv = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)

		# Define the Yellow Colour in HSV
		#RGB
		#[[[222,255,0]]]
		#BGR
		#[[[0,255,222]]]
		"""
		To know which color to track in HSV, Put in BGR. Use ColorZilla to get the color registered by the camera
		>>> yellow = np.uint8([[[B,G,R ]]])
		>>> hsv_yellow = cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)
		>>> print( hsv_yellow )
		[[[ 34 255 255]]
		"""
		lower_yellow = np.array([20,100,100])
		upper_yellow = np.array([50,255,255])

		# Threshold the HSV image to get only yellow colors
		mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
	
		# Bitwise-AND mask and original image
		res = cv2.bitwise_and(crop_img,crop_img, mask= mask)

		# Calculate centroid of the blob of binary image using ImageMoments
		m = cv2.moments(mask, False)
		try:
			#global lidar_flag
			cx, cy = m['m10']/m['m00'], m['m01']/m['m00']

			# Draw the centroid in the resultantt image
			cv2.circle(res,(int(cx), int(cy)), 5,(0,0,255),-1)
			
			error_x = cx - width / 2;
			twist_object = Twist();
			twist_object0 = Twist();
			twist_object.linear.x = 0.5;
			twist_object.angular.z = -error_x / 50;
			if(lidar_flag == 0):
				self.moverobot_object.move_robot(twist_object)
			elif(lidar_flag == 1):
				self.moverobot_object.move_robot(twist_object0)

			
		except ZeroDivisionError: # When no line is found - Recovery Behaviour
			rospy.loginfo("Finding Target...")
			twist_object = Twist()
			twist_object.angular.z = 1
			if(lidar_flag == 0):
				self.moverobot_object.move_robot(twist_object)
			elif(lidar_flag == 1):
				self.moverobot_object.move_robot(twist_object0)

		

		cv2.imshow("Original", cv_image)
		cv2.imshow("RES", res)
		cv2.waitKey(1)


	def clean_up(self):
		self.moverobot_object.clean_class()
		cv2.destroyAllWindows()

	# def lidar_callback(self, msgs):
	# 	print '-------------------------------------------'
 #    	print 'Range data at 0 deg:   {}'.format(msgs.ranges[0])
 #    	print 'Range data at 15 deg:  {}'.format(msgs.ranges[15])
 #    	print 'Range data at 345 deg: {}'.format(msgs.ranges[345])
 #    	print '-------------------------------------------'
 #    	if msgs.ranges[0]>threshold and msgs.ranges[15]>threshold and msgs.ranges[345]>threshold:
 #    		pass
 #    	else :
 #    		twist = Twist()
 #    		twist.linear.x = 0
 #    		twist.linear.y = 0
 #    		twist.linear.z = 0
 #    		twist.angular.x = 0
 #    		twist.angular.y = 0
 #    		twist.angular.z = 0
 #    		self.move_robot(twist)

def main():
	rospy.init_node('line_following_node', anonymous=True)
	line_follower_object = LineFollower()
	threshold = 0.8
	lidar_sub = rospy.Subscriber("/scan", LaserScan, lidar_callback)
	rate = rospy.Rate(5)
	ctrl_c = False

	def shutdownhook():
	# works better than the rospy.is_shut_down()
		line_follower_object.clean_up()
		rospy.loginfo("shutdown time!")
		ctrl_c = True

	rospy.on_shutdown(shutdownhook)

	while not ctrl_c:
		rate.sleep()


if __name__ == '__main__':
	main()
