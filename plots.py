#!/usr/bin/env python3
from matplotlib import pyplot as plt
import numpy as np
from scipy.spatial.transform import Rotation as R

f = open('states.npy', 'rb')
state = np.load(f)
# state structure:
# 0-3 base orientation quaternion or Euler крен тангаж рыскание
# 4-6 base position
# 7-9 left front
# 10-12 right front
# 13-15 left hind
# 16-18 right hind

f = open('t.npy', 'rb')
t = np.load(f)
# data resize
FIRST_IND = 10
t = t[FIRST_IND:]
state = state[:,FIRST_IND:]

# # Euler angles
# q = np.zeros((np.shape(state[0])[0],4))
# for i in np.arange(np.shape(state[0])[0]):
#     q[i][0] = state[1][i]
#     q[i][1] = state[2][i]
#     q[i][2] = state[3][i]
#     q[i][3] = state[0][i]

# q = R.from_quat(q).as_euler('xyz', degrees=True)
# roll = np.zeros(np.shape(state[0])[0]) 
# pitch = np.zeros(np.shape(state[0])[0]) 
# yaw = np.zeros(np.shape(state[0])[0]) 
# for i in np.arange(np.shape(state[0])[0]):
#     roll[i] = q[i][0]
#     pitch[i] = q[i][1]
#     yaw[i] = q[i][2]

# plt.figure(figsize=(10,5))
# plt.subplot(3,1,1)
# plt.title("Ориентация тела")
# plt.grid(1)
# plt.plot(t, roll, linewidth='2')
# plt.ylabel("Крен, [град.]")

# plt.subplot(3,1,2)
# plt.grid(1)
# plt.plot(t, pitch, linewidth='2')
# plt.ylabel("Тангаж, [град.]")

# plt.subplot(3,1,3)
# plt.grid(1)
# plt.plot(t, yaw, linewidth='2')
# plt.ylabel("Рыскание, [град.]")

# plt.xlabel("время [сек]")   
# plt.savefig("orientation.pdf",bbox_inches='tight', pad_inches=0)

# plt.figure(figsize=(10,5))
# plt.subplot(3,1,1)
# plt.title("Положение тела")
# plt.grid(1)
# plt.plot(t, state[4], linewidth='2')
# plt.ylabel("X, [м.]")

# plt.subplot(3,1,2)
# plt.grid(1)
# plt.plot(t, state[5], linewidth='2')
# plt.ylabel("Y, [м.]")

# plt.subplot(3,1,3)
# plt.grid(1)
# plt.plot(t, state[6], linewidth='2')
# plt.ylabel("Z, [м.]")

# plt.xlabel("время [сек]")   
# plt.savefig("coordinates.pdf",bbox_inches='tight', pad_inches=0)

# plt.figure(figsize=(10,5))
# plt.subplot(3,1,1)
# plt.title("Передняя левая нога, углы.")
# plt.grid(1)
# plt.plot(t, state[7]*180/np.pi, linewidth='2')
# plt.ylabel("$q_1$, [град.]")

# plt.subplot(3,1,2)
# plt.grid(1)
# plt.plot(t, state[8]*180/np.pi, linewidth='2')
# plt.ylabel("$q_2$, [град.]")

# plt.subplot(3,1,3)
# plt.grid(1)
# plt.plot(t, state[9]*180/np.pi, linewidth='2')
# plt.ylabel("$q_3$, [град.]")

# plt.xlabel("время [сек]")   
# plt.savefig("q_leg_fl.pdf",bbox_inches='tight', pad_inches=0)

# plt.figure(figsize=(10,5))
# plt.subplot(3,1,1)
# plt.title("Передняя правая нога, углы.")
# plt.grid(1)
# plt.plot(t, state[10]*180/np.pi, linewidth='2')
# plt.ylabel("$q_1$, [град.]")

# plt.subplot(3,1,2)
# plt.grid(1)
# plt.plot(t, state[11]*180/np.pi, linewidth='2')
# plt.ylabel("$q_2$, [град.]")

# plt.subplot(3,1,3)
# plt.grid(1)
# plt.plot(t, state[12]*180/np.pi, linewidth='2')
# plt.ylabel("$q_3$, [град.]")

# plt.xlabel("время [сек]")   
# plt.savefig("q_leg_fr.pdf",bbox_inches='tight', pad_inches=0)


# plt.figure(figsize=(10,5))
# plt.subplot(3,1,1)
# plt.title("Задняя левая нога, углы.")
# plt.grid(1)
# plt.plot(t, state[13]*180/np.pi, linewidth='2')
# plt.ylabel("$q_1$, [град.]")

# plt.subplot(3,1,2)
# plt.grid(1)
# plt.plot(t, state[14]*180/np.pi, linewidth='2')
# plt.ylabel("$q_2$, [град.]")

# plt.subplot(3,1,3)
# plt.grid(1)
# plt.plot(t, state[15]*180/np.pi, linewidth='2')
# plt.ylabel("$q_3$, [град.]")

# plt.xlabel("время [сек]")   
# plt.savefig("q_leg_hl.pdf",bbox_inches='tight', pad_inches=0)


# plt.figure(figsize=(10,5))
# plt.subplot(3,1,1)
# plt.title("Задняя правая нога, углы.")
# plt.grid(1)
# plt.plot(t, state[16]*180/np.pi, linewidth='2')
# plt.ylabel("$q_1$, [град.]")

# plt.subplot(3,1,2)
# plt.grid(1)
# plt.plot(t, state[17]*180/np.pi, linewidth='2')
# plt.ylabel("$q_2$, [град.]")

# plt.subplot(3,1,3)
# plt.grid(1)
# plt.plot(t, state[18]*180/np.pi, linewidth='2')
# plt.ylabel("$q_3$, [град.]")

# plt.xlabel("время [сек]")   
# plt.savefig("q_leg_hr.pdf",bbox_inches='tight', pad_inches=0)

