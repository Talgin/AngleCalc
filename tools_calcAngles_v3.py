import math
import serial
import time
import struct
import decimal
import json
import requests
hPI = 180	# Half of PI
PI = 3.14159265	# PI value
def calculateX(x, y, x1, y1, xRes, yRes, FOV):
	theta = FOV/2	# Central angle of the view
	xppAngle = FOV/xRes	# Angle per Pixel by x
	xImgCenter = x + (x1/2)	# Center of an Image by x
	#print(xImgCenter)
	xCentView = xRes/2	# Center of view by x
	#print(xCentView)
	if xImgCenter > xCentView:	# if image is on the right side of the view
		xFromCenter=xImgCenter - xCentView	# Calculate the distance from center by x
		#print(xFromCenter)
		tangensPhi = (2*xFromCenter*math.tan(theta*PI/hPI))/xRes	# Tangent angle
		#print(tangensPhi)
		xAngle = (hPI*tangensPhi)/PI	# Angle from the center of view by x
	else:
		xFromCenter = xCentView - xImgCenter	# Calculate the distance from center by x
		#print(xFromCenter)
		tangensPhi = (2*xFromCenter*math.tan(theta*Pi/hPI))/xRes	# Tangent angle
		#print(tangensPhi)
		xAngle = (hPI*tangensPhi)/PI	# Angle from the center of view by x
	#print(xAngle)	# Output angle by x
	return xAngle
	
def calculateY(x, y, x1, y1, xRes, yRes, FOV):
	theta = FOV/2	# Central angle of the view
	yppAngle = FOV/yRes	# Angle per Pixel by y
	yImgCenter = y + (y1/2)	# Center of an Image by y
	#print(yImgCenter)
	yCentView = yRes/2	# Center of view by y		
	#print(yCentView)
	if yImgCenter > yCentView:
		yFromCenter = yImgCenter - yCentView	# Calculate the distance from center by y
		#print(yFromCenter)
		tangensPhi = (2*yFromCenter*math.tan(theta*PI/hPI))/yRes	# Tangent angle
		#print(tangensPhi)
		yAngle = (hPI*tangensPhi)/PI	# Angle from the center of view by y
	else:
		yFromCenter = yCentView - yImgCenter	# Calculate the distance from center by y
		#print(yFromCenter)
		tangensPhi = (2*yFromCenter*math.tan(theta*Pi/hPI))/yRes	# Tangent angle
		#print(tangensPhi)
		yAngle = (hPI*tangensPhi)/PI	# Angle from the center of view by y	
	#print(yAngle)	# Output angle by y	
	return yAngle

def send(neim, speed, valX, valY):
	try:
		arduino = serial.Serial(neim,speed)
		time.sleep(1)
		print("Connection to " + neim + " established succesfully!\n")
	except Exception as e:
		print(e)
	
	try:
		print(arduino.name)
		valX = decimal.Decimal(valX)
		valY = decimal.Decimal(valY)		
		data1 = struct.pack('f', round(valX, 3))
		data2 = struct.pack('f', round(valY, 3))
		data = data1+data2
		arduino.write(data)		
		#time.sleep(1)
	except Exception as e:
		print(e)
	arduino.close()
	print("Value written to port: '%s'"%data)

def sendRPC(fr, spdA, stpA, spdB, stpB):
        #muv, trt, fr, spdA, stpA, spdB, stpB
        #url = "http://localhost:8383"
        url = "http://192.168.1.254:8383"
        headers = {'content-type': 'application/json'}

        move = {"forward":True,"backward":False,"left":False,"right":False}
        turret = {"up":False,"down":False,"left":False,"right":False}
        #params = {"move":move,"turret":turret,"fire":False, "speedA": 0, "stepA": 0,"accelA": 0.0, "speedB": 10000,"stepB": 5000, "accelB": 4000.0 }
        #params = {"move":move,"turret":turret,"fire":False, "speedA": 20000, "stepA": 5000,"accelA": 4000.0, "speedB": -20000,"stepB": -7000, "accelB": 4000.0 }
        params = {"move":move,"turret":turret,"fire":False, "speedA": spdA, "stepA": stpA,"accelA": 4000.0, "speedB": spdB,"stepB": stpB, "accelB": 0.0 }
        payload = {
                "method": "sendControl",
                "params": params,
                "jsonrpc": "2.0",
                "id": 1,
                }
        response = requests.post(url, data=json.dumps(payload), headers=headers).json()
        print(json.dumps(payload))
        print(json.dumps(response))
	 
