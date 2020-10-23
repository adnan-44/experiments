import pyautogui, time
time.sleep(5)
num = 22
while num > 0:
	pyautogui.typewrite('Message sent')
	pyautogui.press("enter")
	num = num - 1
