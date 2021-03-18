# Installing Turtlebot3

## Pre-Requisites
1. Ubuntu 18.04
	- To check run the following command:
		```sh
		lsb_release -a # The output must have Release: 18.04
		```

2. Have git installed
    - To check: 
		```sh
		git --version # Should execute without errors
		```
	- If not installed run:
		```sh
		sudo apt install git
		```
	
2. ROS Melodic Installed
	- To check, run the following commands:
		```sh
		echo $ROS_PACKAGE_PATH # Output Must be /opt/ros/melodic/share[:...]
		```
3. Have a Catkin Workspace
	- To check run the following Commands:
		```sh
		cd ~/catkin_ws/ # Or move to wherver your catkin workspace is located
		catkin_make # This should run, without any errors to 100% Completion
		```

## Installing Turtlebot3 and other required Packages
0. Update  Packages and Repositories
	```sh
	sudo apt update && sudo apt upgrade
	```
1. Installing turtlebot3 and turtlebot3-msgs
	```sh
	sudo apt install ros-melodic-dynamixel-sdk
	sudo apt install ros-melodic-turtlebot3-msgs
	sudo apt install ros-melodic-turtlebot3
	```

2. Set turtlebot3 name
   ```sh
   echo "export TURTLEBOT3_MODEL=waffle_pi" >> ~/.bashrc
   source ~/.bashrc
   ```

3. Installing turtlebot3-simulations
	```sh
	cd ~/catkin_ws/src/
	git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
	cd ~/catkin_ws && catkin_make
	reboot # Will restart your sytem
	```


4. Test if everyhing works
	```sh
	cd ~/catkin_ws
	source devel/setup.bash
	roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
	```