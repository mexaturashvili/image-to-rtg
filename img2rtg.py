import json
import base64
import cv2
import pyperclip



def fix_data():
	for connector in data:
		del connector[-1]

def paint(x, y, rgb):
	for connector in data:
		if connector[-1] == (x, y):
			connector[2] = {"RGB":rgb}


data = []


loc = input("image location:")
img = cv2.imread(loc)
x = int(input("X: "))
y = int(input("Y: "))

if not x > 0 or not y > 0:
	print("x and y values must be over 0")
	exit()



img = cv2.resize(img, (x, y), dst=None, fx=0, fy=0, interpolation=cv2.INTER_LINEAR)

cv2.imwrite("images/test.png", img)






total_index = 0
y_connector_indexes = []
for y_index in range(1, y+1): # generate Y line
	total_index += 1
	y_connector_indexes.append(total_index)
	if y_index == 1:
		data.append(["Connector",[], [], (1, y_index)])
	elif y_index == 2:
		data.append(["Connector",[["5","6",total_index-1]],[], (1, y_index)])
	else:
		data.append(["Connector",[["5","4",total_index-1]],[], (1, y_index)])


for y_index in y_connector_indexes:
	for x_index in range(1, x): # generate X line on every Y connector
		total_index += 1
		if y_index == 1:
			if x_index == 1:
				data.append(["Connector",[["5","1", y_index]],[], (x_index+1, y_index)])
			else:
				data.append(["Connector",[["5","4",total_index-1]],[], (x_index+1, y_index)])
		else:
			if x_index == 1:
				data.append(["Connector",[["5","2", y_index]],[], (x_index+1, y_index)])
			else:
				data.append(["Connector",[["5","4",total_index-1]],[], (x_index+1, y_index)])






y_cursor = 1
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
for y in img:
	x_cursor = 1
	for x in y:
		rgb = [int(x) for x in x]
		paint(x_cursor, y_cursor, rgb)
		x_cursor += 1
	y_cursor += 1



fix_data()



jsondata = json.dumps(data, separators=(',', ':'))
encodeddata = base64.b64encode(bytes(jsondata.encode())).decode()


# with open("save.json", "w") as f:	
# 	f.write(jsondata)


print(jsondata)

print("\n"*3)
print("="*20)
print(encodeddata)
pyperclip.copy(encodeddata)
print("="*5 + "THE BASE64 CODE WAS COPIED ON CLIPBOARD" + "="*5)
print("="*5 + "PASTE IT IN THE GAME TO USE" + "="*5)


input("press enter to close")