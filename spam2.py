import pyautogui, time
time.sleep(5)
f = open("hello.txt",'r')
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
f.close()
f1 = open("hello1.txt",'r')
for word in f1:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
