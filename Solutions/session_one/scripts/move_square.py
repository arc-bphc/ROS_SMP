#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg  import Int32

var = Twist()

def callback_function(given):
    size = given.data
    for count in range(4):
        #move forward
        var.linear.x = 0.2
        var.angular.z = 0
        pub_vel.publish(var)
        rospy.sleep(size)
        #stop
        var.linear.x=0
        var.angular.z=0
        pub_vel.publish(var)
        rospy.sleep(2)
        #rotate by 90 deg
        var.linear.x = 0
        var.angular.z = 0.5
        pub_vel.publish(var)
        rospy.sleep(3)
        #stop
        var.linear.x=0
        var.angular.z=0
        pub_vel.publish(var)
        rospy.sleep(2)
        rospy.loginfo(count)  
    var.linear.x=0
    var.angular.z=0
    pub_vel.publish(var)
    print("all done")


rospy.init_node('node_square')
pub_vel = rospy.Publisher('/cmd_vel',Twist,queue_size=2)
rospy.Subscriber('/your_word_is_your_wand',Int32,callback_function)
rospy.spin()