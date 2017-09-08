import win32com.client
import time


def openExcelSheet():
    xl = win32com.client.gencache.EnsureDispatch("Excel.Application")
    xl.Visible = True
    Workbook = xl.Workbooks.Add()
    Sheets = Workbook.Sheets
    liveExportData(Sheets)

def liveExportData(Sheets):
        time.sleep(1)
        Sheets(1).Cells(1, 1).Value = 'Kam-Spec 2017'
        Sheets(1).Cells(2,1).Value = 'Date: ' + time.strftime('%x')
        Sheets(1).Cells(2,3).Value = 'Time: ' + time.strftime('%X')
        time.sleep(.5)

openExcelSheet()