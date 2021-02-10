from openpyxl import load_workbook
workbook = load_workbook(filename='TradingJournal.xlsx')
worksheet = workbook['Trade Log']
cell_c4 = worksheet['C4'].value
print(cell_c4)

worksheet['B7'] = '2/10/2021'
worksheet['C7'] = 'TSLA'
worksheet['D7'] = 'B'
worksheet['E7'] = 100
worksheet['F7'] = 800
workbook.save(filename='TradingJournal-updated.xlsx')