import pyautogui

size = pyautogui.size()         # 현재 화면의 스크린 사이즈를 가져옴
print(size)                     # size[0] : width, size[1] : height
position = pyautogui.position() # 현재 커서의 위치 가져옴
print(position)