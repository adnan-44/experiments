import pyautogui, time
time.sleep(5)
#f = open("hello.txt",'r')
num = 100
#for word in f:
while num > 0:
	pyautogui.typewrite('You do not have time, wait')
	pyautogui.press("enter")
	num = num - 1
