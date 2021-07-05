# 이미지 삽입

from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("image.png")

# C3 위치에 이미지 파일 삽입
ws.add_image(img, "C3")

wb.save("sample_image.xlsx")