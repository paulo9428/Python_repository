import csv, codecs
from openpyxl.chart import (
    Reference,
    BarChart
)

sheet3 = book.create_sheet()
sheet3.title = "세번째 시트"
rows = []

with codecs.open('./meltop100.csv', 'r', 'utf-8') as meltop:
    reader = csv.reader(meltop, delimiter=',', quotechar='"')
    for i, row in enumerate(reader):
        if i > 1 and i < 12:
            rows.append([row[1], row[3]])
            
for row in rows:
    sheet3.append(row)

datax = Reference(sheet, min_col=2, 
		min_row=1, max_col=2, max_row=5)
categs = Reference(sheet, min_col=1,
				 min_row=1, max_row=5)

chart = BarChart()
chart.add_data(data=datax)
chart.set_categories(categs)

chart.legend = None  # 범례
chart.varyColors = True
chart.title = "좋아요 차트"

sheet.add_chart(chart, "A3")





book.save("./output3.xlsx")