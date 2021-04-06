# 2. Messages

- Originally authored by: [Jai Krishna](https://github.com/TextZip)

## 1.1 Introduction to Messages

As explained before data is sent via messages inside topics. ROS has a rich set of predefined messages that can be used. Messages can contain premitive datatypes or can be composed of multiple primitve datatypes.

### Some basic Commands

1. Determine the type of message used by a node

```sh
rosnode info /<node_name>
``` 

1. Get information about a particular message type

```sh
rosmsg show <package_name>/<message_name>
```

example:

```sh
> rosmsg show geometry_msgs/PointStamped

std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
geometry_msgs/Point point
  float64 x
  float64 y
  float64 z
```

## 2.1 Writing Custom Messages

In situations where standard messages don't do the job, you can create your own message types using the following steps.

(Refer to main tutorial for now, will fill it up later)
