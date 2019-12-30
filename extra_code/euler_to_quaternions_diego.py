#! /usr/bin/env python
import rospy
from math import pi
from tf.transformations import euler_from_quaternion, quaternion_from_euler

# Usamos funcion de tf.transformations (ROS) e imprimimos resultado
def convertir(roll,pitch,yaw):
	quat = quaternion_from_euler (roll,pitch,yaw)
	print "R=",roll,"P=",pitch,"Y=",yaw,"-> QUAT=",quat

# Varios cuaternios basicos
convertir(0,0,0)
convertir(pi/2,0,0)
convertir(0,pi/2,0)
convertir(0,0,pi/2)
convertir(pi/2,pi/2,pi/2)
 
