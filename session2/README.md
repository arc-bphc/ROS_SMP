# 1. Topics, Publishers & Subscribers

- Originally authored by: [Jai Krishna](https://github.com/TextZip)

## 1.1 Introduction to Topics

ROS Nodes communicate with each other via communication channels called "Topics", further messages are passed between nodes through topics. Every topic has a message type that it supports communication over. Nodes can subscribe to a topic to listen to data from other nodes or publish to topics to send data to other nodes which are subscribed to a given topic.

### Some basic Commands

1. Check for active Topics

```sh
rostopic list
```

2. More information about a topic

```sh
rostopic info /<topic_name>
```

3. Publishing to a topic at a rate of x Hz

```sh
rostopic pub -r <x> /<topic_name> /<message_type> [args] 
```

4. Listening to a topic

```sh
rostopic echo /<topic_name>
```

## 1.2 Writing a publisher in Python

```py
#! /usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('node_name')
pub = rospy.Publisher('/topic_name', String, latch=True, queue_size=10)

r = rospy.rate(10) # Rate at which you wanna publish, in Hz

while not rospy.is_shutdown():
    pub.publish("Python mother, do you speak it.")
    r.sleep() # Why not time.sleep( 1.0f / r)
```

## 1.3 Writing a subscriber in Python

```py

import rospy
from std_msgs.msg import String

def callback_function(data):
    result = data.data # Why not just data?

rospy.init_node('node_name')
rospy.Subscriber('/topic_name', String, callback_function) # Why not callback_function() ?

rospy.spin() # Why not a while loop?
```

> [Next](./Messages.md)