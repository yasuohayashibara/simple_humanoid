#!/usr/bin/env python3

import pybullet as p
from time import sleep

TIME_STEP = 0.001

physicsClient = p.connect(p.GUI)
p.setGravity(0, 0, -9.8)
p.setTimeStep(TIME_STEP)

planeId = p.loadURDF("URDF/plane.urdf", [0, 0, 0])
RobotId = p.loadURDF("URDF/simple_humanoid.urdf", [0, 0, 0])

for joint in range(p.getNumJoints(RobotId)):
  p.setJointMotorControl(RobotId, joint, p.POSITION_CONTROL, 0)

index = {p.getBodyInfo(RobotId)[0].decode('UTF-8'):-1,}
for id in range(p.getNumJoints(RobotId)):
	index[p.getJointInfo(RobotId, id)[12].decode('UTF-8')] = id

print(index)

angle = 0
angle2 = 0.19
velocity = 1.5
velocity2 = 1.5
while p.isConnected():
  angle += velocity * TIME_STEP
  angle2 += velocity2 * TIME_STEP
  p.setJointMotorControl2(RobotId, index['waist_link' ], p.POSITION_CONTROL, -angle)
  p.setJointMotorControl2(RobotId, index['left_thigh_pitch_link' ], p.POSITION_CONTROL,  angle2 * 0.5)
  p.setJointMotorControl2(RobotId, index['right_thigh_pitch_link'], p.POSITION_CONTROL, -angle2 * 0.5)
  if angle >= 0.2:
    velocity *= -1.0
  if angle <= -0.2:
    velocity *= -1.0
  if angle2 >= 0.2:
    velocity2 *= -1.0
  if angle2 <= -0.2:
    velocity2 *= -1.0

  p.stepSimulation()
  sleep(TIME_STEP)

