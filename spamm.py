import pyautogui, time
time.sleep(5)
#f = open("hello.txt",'r')
num = 3
#for word in f:
while num > 0:
	pyautogui.typewrite('kumar')
	pyautogui.press("enter")
	num = num - 1
	#time.sleep(0.9)
