#!/usr/bin/env python

import rospy
from geometry_msgs.msg._Twist import Twist

""" Example of how to set attributes in ROS messages """

def twist_fill():
	WhatA = Twist()
	WhatA.linear.x = 5.872378
	WhatA.linear.y = 3.094386
	WhatA.linear.z = 6.250895
	WhatA.angular.x = 7.382474
	WhatA.angular.y = 3.839298
	WhatA.angular.z = 2.783469
	return WhatA
	
	
	
