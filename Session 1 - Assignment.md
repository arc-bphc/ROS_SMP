# Session 1 - Assignment

**NOTE- The "turtlesim_node" and "turtle_teleop_key" nodes are part of the turtlesim package, make sure its installed before attempting questions 1 and 2**

1) In a terminal start the **turtlesim_node** with node name as "**my_node_1**" in the namespace "**name**". In a seperate terminal start the **turtle_teleop_key** with node name as "**my_node_2**" without any namespaces, and remap the topic such that it can send telemetry data to the turtlesim_node and move the turtle around.

**Kill all previous nodes before starting this question**

2) In a new terminal start the turtlesim_node with node name "turtles" without any namespaces. In a seperate terminal copy paste the following command

```bash
rosservice call /spawn "x: 0.0
y: 0.0
theta: 0.0
name: 'turt'"
```

*(Do not worry if you do not understand the command it will be covered in the later classes) If everything went fine you should see a new turtle in your turtlesim_node. Now, figure out a way to use turtle_teleop_key to control the 2nd turtle.*

**Kill all previous nodes before starting this question, also run the following command before starting this exercise to start the turtlebot3 in gazebo:** 
```bash
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```
3) Create a new package called **session_one** with **rospy** as a dependency, create a new python script called "**move_square.py**" which when executed will listen to a topic called "**/your_word_is_your_wand**" which has a message type of "**std_msgs/Int32**" once it recieves data from the above mentioned topic, it should direct the turtlebot3 to perform a square with side length being propotional to the integer recieved from the above mentioned topic.

**Kill all previous nodes before starting this question, also run the following command before starting this exercise to start the turtlebot3 in gazebo:** 
```bash
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```

4) In the previously created package, create a custom message named "**JangoFett.msg**" it should have the following structure:
```bash
Int32 side
String shape
```
now, create a new python script called "**move_upgraded.py**" it should listen to the topic called "**/darkside**" which is based on the custom message you created "**JangoFett.msg**", if the shape contains "**circle**" the turtlebot3 should move in a circle where the peremter is propotional to the integer entered in the "**side**", if the shape "**square**", the turtlebot3 should move in a square where the side length is propotional to the integer entered in the "**side**"

**NOTE: The square and circle shapes need not be perfect**

**Kill all previous nodes before starting this question, also run the following command before starting this exercise to start the turtlebot3 in gazebo:**

```bash
roslaunch turtlebot3_gazebo turtlebot3_house.launch
```

5) In the previously created package, create a service server called "**/Arda**" which can be called using an Empty message. Once called the service server has to send back a list which contains the index of the highest and lowest laser scan readings(in that order) from the turtlebot3.


6) Create a package "**custom_service_assignment**"
Launch the **turtlebot3_house.launch** launch file
Optional: Create a launch file "**custom_service_launch.launch**" to start the server and client

Write a **custom server**:
request: **distance** variable: to move the turtlebot for the specified distance in Gazebo.
response: **success** flag ( to inform if the required distance was travelled by the bot)
**additional_message** ( to give any additional information. eg: if the bot failed to cover the distance due to an obstacle)

Your code needs to check for obstacles directly in front of the bot and stop the bot before it hits an obstacle. If the bot is stoppped, then the successs flag should be flase and an appropriate additional_message should be sent.
(Hint: for calculating the distance use the /odom topic)

7) Create an **action server** that when launched will accept a goal in **seconds** and **record odometry data** from the turtlebot for the number of seconds mentioned in the goal, while sending the current odometry reading once every second as **feedback**. Once the specified amount of time has passed, the **action server** should send all the collected odometry data in a list as the **result**.

Also create the required action client to call the above server.

8) For your final assignment, create a python script that would let you do everything from Q4, along with the added features of Q7. Also create a client that will call all the required services and actions. For example,

**compound_server.py**:

- Publisher cmd_vel
- Action server for odometry
- Service server for Shape based moment

**compound_client.py**:
- Action client
- Service client