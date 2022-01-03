#! /usr/bin/env python3

import rospy
from session_one.srv import laser_service,laser_serviceResponse
from sensor_msgs.msg import LaserScan
laser_max = 0.00
laser_min = 0.00


def laser_callback(data):
    global laser_sub
    global laser_max
    global laser_min
    laser_max = max(data.ranges)
    laser_min = min(data.ranges)
    # print(laser_max)
    # print(laser_min)
    laser_sub.unregister()


def service_callback_function(request):
    laser = laser_serviceResponse()
    global laser_sub
    global laser_max
    global laser_min
    laser_sub = rospy.Subscriber('scan',LaserScan,callback=laser_callback)
    print(laser_max)
    print(laser_min)
    laser.laser_min.data = laser_min
    laser.laser_max.data = laser_max
    # ,laser_min]
    # laser_serviceResponse.laser_list.append(laser_min)
    return laser


rospy.init_node('arda_service_server_node')
my_service = rospy.Service('/Arda',laser_service,service_callback_function)
rospy.spin()
