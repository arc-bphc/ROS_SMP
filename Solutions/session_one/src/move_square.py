#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
velocity = Twist()
def move_square_callback(data):
    for i in range(4):
        velocity.linear.x=0.10
        velocity.angular.z=0.00
        pub.publish(velocity)
        rospy.sleep(data.data)
        velocity.linear.x=0.00
        velocity.angular.z=0.00
        pub.publish(velocity)
        velocity.linear.x=0.00
        velocity.angular.z=0.20
        pub.publish(velocity)
        rospy.sleep(8)
        velocity.linear.x=0.00
        velocity.angular.z=0.00
        pub.publish(velocity)
    pass

rospy.init_node("move_square_node")

pub = rospy.Publisher('cmd_vel',Twist,latch=True,queue_size=10)

rospy.Subscriber('/your_word_is_your_wand',Int32,callback=move_square_callback)
rospy.spin()