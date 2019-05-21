import calcAngles_v3
import time
# calculating angles of X and Y by x, y position, width-height, x-y resolution, and FOV of camera
valX = calcAngles_v3.calculateX(824, 653, 50, 50, 1366, 768, 60)   # calculate by X
valY = calcAngles_v3.calculateY(824, 653, 50, 50, 1366, 768, 60)   # calculate by Y

# to test the sending you should send boolean for fire (True, False),
# speedA, stepA, speedB, stepB
# {"move":move,"turret":turret,"fire":False, "speedA": 20000, "stepA": 10000,"accelA": 4000.0, "speedB": 0,"stepB": 0, "accelB": 0.0 }
# calcAngles_v3.sendRPC(True, 6000, 700, 4000, 700)

# V1
# command = number of steps
# 2475*20 ~ 90 degrees 8 steps = 1.8 degrees 
# 49500 => 2475 / 90 = 550 steps to reach one degree
# if your object is on 60 degree point you should move 60*27.5=1650 in for loop

# V2
# 4800 ~ 90 degrees
# We can send commands by pulses => dividing 4800 into let's say 200 in one pulse
# In the following for you can see the result of sending 12 pulses
# 200 step at a time this will give us 45 degrees approx. (we can't say exactly)
# because the turret's movement has mechanincal error

#calcAngles_v3.sendRPC(False, 10, 500, 0, 0)

# code to turn vertical turret - try - and + values
calcAngles_v3.sendRPC(False, 0, 0, 10000, 500)
# or
calcAngles_v3.sendRPC(False, 0, 0, -10000, -500)

#time.sleep(3.5) + left - right
#ab = 6
#for x in range(0, 6):
 #   calcAngles_v3.sendRPC(False, 10, 350, 0, 0) # move to the left 6 times by 350 steps each time
    #calcAngles_v3.sendRPC(False, -10, -300, 10000, 1000)
 #   time.sleep(0.9)

#time.sleep(1)
#for x in range(0, 8):
 #   calcAngles_v3.sendRPC(False, -10, -350, 0, 0)   # move to the right 8 times by 350 steps each time
    #calcAngles_v3.sendRPC(False, -10, -300, 10000, 1000)
 #   time.sleep(0.9)

#time.sleep(1)
#for x in range(0, 2):
 #   calcAngles_v3.sendRPC(False, 10, 350, 0, 0) # move to the left 2 times by 350 steps each time
    #calcAngles_v3.sendRPC(False, -10, -300, 10000, 1000)
 #   time.sleep(0.9)    
    #calcAngles_v3.sendRPC(False, -10, -300, -10000, -1000)
  #  print("step = ", x)


#calcAngles_v3.sendRPC(False, -10, -400, 0, 0)
#calcAngles_v3.sendRPC(False, 10, 4800, 0, 0)

