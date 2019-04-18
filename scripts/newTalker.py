#!/usr/bin/env python
import roslib
import rospy
from rospy.numpy_msg import numpy_msg
from sensor_msgs.msg import Image
import numpy
from cv_bridge import CvBridge, CvBridgeError
import cv2
class ImageTalker:
	def __init__(self):
		self.bridge = CvBridge()
		self.image_pub = rospy.Publisher('imgs', Image, queue_size = 1)
	def readImage(self):
		self.image = cv2.imread('/home/fatguru/catkin_ws/1.jpg')
		self.imageMsg = self.bridge.cv2_to_imgmsg(self.image, 'bgr8')				
	def talk(self):
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			self.image_pub.publish(self.imageMsg)
			r.sleep()
def main():
	rospy.init_node('talker')
	imagetalker = ImageTalker()
	imagetalker.readImage()
	imagetalker.talk()

if __name__ == '__main__':
	main()