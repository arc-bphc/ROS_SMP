#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from session_one.msg import JangoFett
import math 


def callback_function(obj):
    var = obj.side.data
    shape = obj.shape.data

    if(shape == 'square'):
        for count in range(4):
        #move forward
            var_cmd.linear.x = 0.2
            var_cmd.angular.z = 0
            pub_cmd.publish(var_cmd)
            rospy.sleep(var)
            #stop
            var_cmd.linear.x=0
            var_cmd.angular.z=0
            pub_cmd.publish(var_cmd)
            rospy.sleep(2)
            #rotate by 90 deg
            var_cmd.linear.x = 0
            var_cmd.angular.z = 0.5
            pub_cmd.publish(var_cmd)
            rospy.sleep(3)
            #stop
            var_cmd.linear.x=0
            var_cmd.angular.z=0
            pub_cmd.publish(var_cmd)
            rospy.sleep(2)
            rospy.loginfo(count)  
        var_cmd.linear.x=0
        var_cmd.angular.z=0
        pub_cmd.publish(var_cmd)
        print("all done")

        #do square
    elif(shape == 'circle'):
        r1 = var/2
        v1 = (0.1/0.3)*r1
        w1 = v1/r1
        t=(3.5*2*math.pi)/w1

        var_cmd.angular.z=0.1
        var_cmd.linear.x=v1
        pub_cmd.publish(var_cmd)
        rospy.sleep(t)
        var_cmd.linear.x=0
        var_cmd.angular.z=0
        pub_cmd.publish(var_cmd)

        #do circle

var_cmd = Twist()
rospy.init_node('mover2')

pub_cmd = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
rospy.Subscriber('/darkside',JangoFett,callback_function)
rospy.spin()