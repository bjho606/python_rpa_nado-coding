# 엑셀 파일 만들기

from openpyxl import Workbook
wb = Workbook()     # 새 워크북 생성
ws = wb.active      # 현재 활성화된 sheet 가져오기
ws.title = "MySheet"    # sheet 의 이름을 변경
wb.save("sample.xlsx")
wb.close()