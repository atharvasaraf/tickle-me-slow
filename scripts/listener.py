#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

class ImageReader:
	def __init__(self):
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber('imgs', Image, self.image_cb)
	
	def image_cb(self, msg):
		try:
			self.cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
			self.gray_image = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2GRAY)
			self.np_image = np.array(self.gray_image) 
			print (self.np_image.shape)
		except CvBridgeError as e:
			print(e)
def main():
	imagereader = ImageReader()
	rospy.init_node('listener')
	try:
		rospy.spin()
	except:
		print("You got trolled")	

if __name__ == '__main__':
	main()


# cv2.imshow('lol', self.cv_image)
# 			cv2.waitKey(0)
# 			cv2.destroyAllWindows()