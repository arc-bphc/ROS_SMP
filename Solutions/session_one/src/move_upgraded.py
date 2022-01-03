#! /usr/bin/env python3

import rospy
from session_one.msg import JangoFett
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32
from std_msgs.msg import String



def move_upgraded_callback(data):
    velocity = Twist()
    if (data.shape.data == "circle"):
        velocity.linear.x=0.20*data.side.data
        velocity.angular.z=0.20
        pub.publish(velocity)
        rospy.sleep((2*3.14)/0.20)
        velocity.linear.x=0.00
        velocity.angular.z=0.0
        pub.publish(velocity)

    elif (data.shape.data == 'square'):
        for i in range(4):
            velocity.linear.x=0.10
            velocity.angular.z=0.00
            pub.publish(velocity)
            rospy.sleep(data.side.data)
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


rospy.init_node("move_upgraded_node")
pub = rospy.Publisher('cmd_vel',Twist,latch=True,queue_size=10)
rospy.Subscriber('/darkside',JangoFett,callback=move_upgraded_callback)
rospy.spin()
