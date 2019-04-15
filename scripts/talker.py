#!/usr/bin/env python
import sys, time
import numpy as np
from scipy.ndimage import filters
import cv2
import roslib
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
VERBOSE = False

class image_feature:
	def __init__(self):
		self.image_pub = rospy.Publisher("/output/image_raw/compressed",
			CompressedImage, queue_size = 1)

		self.subscriber = rospy.Subscriber("/camera/image/compressed",
			CompressedImage, self.callback, queue_size = 1)
		if VERBOSE :
			print "Subscribed to /camera/image/compressed"

	def callback(self, ros_data) :
		if VERBOSE :
			print "received image of type: %s" %ros_data.format

		np_arr = np.fromstring(ros_data.data, np.uint8)
		image_np = cv2.imdecode(np_arr, cv2.CV_LOAD_IMAGE_COLOR)

		msg = CompressedImage()
		msg.header.stamp = rospy.Time.now()
		msg.format = "jpeg"
		msg.data = np.array(cv2.imencode('.jpg', image_np)[1]).tostring()
		self.image_pub.publish(msg)

def talker():
	pub = rospy.Publisher('chatter', String, queue_size = 1)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		hello_str = "hello_world %s" %rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

def main(args):
	ic = image_feature()
	rospy.init_node('image_feature', anonymous=True)

	try:
		rospy.spin()
	except rospy.ROSInterruptException:
		pass

if __name__ == '__main__':
	main(sys.argv)