# panda_diego

![Demo](img/example_1_basico.gif)

Code to show the basic usage of the moveitcommander API in python. 

The Gazebo simulation of the Panda arm is taken from [this repo](https://github.com/erdalpekel/panda_simulation). Please follow those guidelines to install the Panda arm Gazebo simulation 

Example of a the execution of a cartesian path: 

![Cartesian](img/example_cartesian.gif)
___

## Usage

#### Sourcing the repo

```
source robindustrial_ws/devel/setup.bash
```

#### Gazebo simulation of the basic Panda + Moveit config + Rviz plugin  

```
roslaunch panda_diego simulation_diego.launch
```
#### Basic python programs to interface moveit_commander API

Forward kinematics plan and execution:
```
rosrun panda_diego forward_kinematics.py
```
Inverse kinematics plan and execution (move joints):
```
rosrun panda_diego IK_destination pose.py
```
Cartesian path (IK) plan and execution (move linear):
```
rosrun panda_diego IK_cartesian_path.py
```

## TO DO List as December 30, 2019

* Add Pick and place example
* Add more complex Gazebo scenes + Perception



