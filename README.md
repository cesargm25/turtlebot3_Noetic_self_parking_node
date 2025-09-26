# Self-Parking Robot Controller (ROS)

This repository contains a **ROS1 (Python)** node that drives a differential robot, specifically the Turtlebot3 Burger, to a predefined goal position using odometry.  
The node subscribes to `/odom` and publishes velocity commands to `/cmd_vel` to navigate the robot toward `(x=1.5, y=1.5)`.

---

## Features

- Subscribes to `/odom` to get the robot’s position and orientation.
- Publishes velocity commands to `/cmd_vel` (`geometry_msgs/Twist`).
- Two-step motion strategy:
  1. Move along the **x-axis** until reaching the target.
  2. Rotate 90° and move along the **y-axis**.
- Simple logic for reaching a fixed goal.
- It was meant to be a simple exercise for explanation. 

---

## Requirements

- **ROS 1 (Noetic recommended)**
- Python 3
- Standard ROS packages:
  - `geometry_msgs`
  - `nav_msgs`
  - `tf`

Your robot (or simulator, e.g., TurtleBot in Gazebo) must publish odometry on `/odom` and accept velocity commands on `/cmd_vel`.

---

## Installation

Clone the script into your ROS workspace (in my case is turtlebot3_ws):

```bash
cd ~/catkin_ws/src
git clone https://github.com/turtlebot3_ws/self_parking_robot.git
cd ~/catkin_ws
catkin_make
