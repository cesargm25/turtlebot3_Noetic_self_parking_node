#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point 
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import radians
import math


print("at least till here is gut")

x_1 = 0.0
y_1 = 0.0
betha = 0.0
start=0
goal = Point()
goal.x = 1.5
goal.y = 1.5

class vel_manipulator:

    def __init__(self):
        self.pub_topic_name ="/cmd_vel" # define the topic to publish
        self.sub_topic_name ="/odom" # define the topic to subscribe
        self.pub = rospy.Publisher(self.pub_topic_name, Twist, queue_size=10) # publishing in Twist
        self.number_subscriber = rospy.Subscriber(self.sub_topic_name, Odometry, self.odo_callback) #
        self.velocity_msg = Twist()
        print(self.velocity_msg)
       

    
    def odo_callback(self,msg):

        
        global x_1, y_1, betha, goal,start
        x_1 = msg.pose.pose.position.x
        y_1 = msg.pose.pose.position.y
        rot_q = msg.pose.pose.orientation
        (roll, pitch, betha) = euler_from_quaternion ([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

# initial location
        if start == 0 and betha > 0.1:
          print('thi is start ',start)
          print('this is ',betha)
          angle_goal=0
          rad_goal=angle_goal*math.pi/180
          self.velocity_msg.angular.z= 0.3*(rad_goal-betha)
        else:

       
# speed /movement in +x
         if goal.x > 0:
            if abs(goal.x - x_1)>0.1:
                if goal.x > x_1:
                  print( 'position  ', x_1)
                  print('goal ', goal.x)
                  self.velocity_msg.linear.x = 0.15
                  self.velocity_msg.angular.z = 0.0
                  start=+1
                else:
                  print( 'position  ', x_1)
                  print('goal ', goal.x)
                  self.velocity_msg.linear.x = -0.15
                  self.velocity_msg.angular.z = 0.0
                  start=+1
                   
            else:
                self.velocity_msg.linear.x = 0.0
                start=+1
              
 # -speed / movement in -x               
         else:
            if goal.x <= x_1:
                if abs(goal.x)-abs(x_1)<0:
                  self.velocity_msg.linear.x = 0.15
                  self.velocity_msg.angular.z = 0.0
                  print('2')
                  start=+1
                else:
                 print( 'position 1', x_1)
                self.velocity_msg.linear.x = -0.15
                self.velocity_msg.angular.z = 0.0
                start=+1
            else:
                
                self.velocity_msg.linear.x = 0.0
                self.velocity_msg.angular.z = 0.0
                start=+1

        print(goal.x, goal.y, x_1, y_1)
               
        
#____________________ turn()____________________________
#intial condition for turnning
        if abs(goal.x -x_1) <= 0.1:
          rot_q = msg.pose.pose.orientation
          (roll, pitch, betha) = euler_from_quaternion ([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
          angle_goal=90
          rad_goal=angle_goal*math.pi/180
          self.velocity_msg.angular.z= 0.3*(rad_goal-betha)
          start=+1
# ____________turn 
          if abs(rad_goal-betha) <= 0.1:
              if goal.y > y_1:
               if (goal.y-y_1)>0.1:
            
                 self.velocity_msg.linear.x = 0.1
                 self.velocity_msg.angular.z = 0.0
                 start=+1
               else:
                  self.velocity_msg.linear.x = 0.0
                  self.velocity_msg.angular.z = 0.0
                  start=+1
#__________clockwise turn
              else:
               if (goal.y-y_1)<0.1: 
                 
                 self.velocity_msg.linear.x = -0.1
                 self.velocity_msg.angular.z = 0.0
                 start=+1
               else:
                  self.velocity_msg.linear.x = 0.0
                  self.velocity_msg.angular.z = 0.0
                  start=+1
                  
                  
              
        print('the current position is  ',x_1,'  ',y_1)
        self.pub.publish(self.velocity_msg)



if __name__ =='__main__':
    node_name ="self_parking"
    rospy.init_node(node_name) # Ros function to initialize a Ros node
    vel_manipulator_instance = vel_manipulator()
    rospy.spin() # It enters a loop that continues to run until the ROS node is shutdown externally
    print('You got it')


