import rospy
from std_msgs.msg import String
import threading
class listen_accumulator:
	def __init__(self):
		rospy.init_node('listener_accumulator', anonymous=True)

		self.listen()
		self.chatter_data = ''
		self.pub = rospy.Publisher('chatter_repeated',String, queue_size=10)
		self.rate = rospy.Rate(.333)
		msg = String()
		while not rospy.is_shutdown():
			msg.data = self.chatter_data
			rospy.loginfo(msg.data)
			self.pub.publish(msg)
			self.rate.sleep()



	def listen(self):
		sub = rospy.Subscriber('chatter',String,self.callback)


	def callback(self,data):
		self.chatter_data = data
		print("hello")
if __name__ == '__main__':
	try:
		x=listen_accumulator()
	finally:
		pass
