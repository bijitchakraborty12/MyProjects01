# In your python terminal cd into the directory having the excel file. 
import xlrd
book = xlrd.open_workbook("myBook_01.xlsx") # in my case the directory contains the excel file named excel.xls

# Now to print the number of worksheets in the excel file 
print("The number of worksheets are ", book.nsheets)

# Now the names of the worksheets in excel file 
print("The names of worksheets are", book.sheet_names()) # returns an array of names 

# Choose a specific workbook to import data 
sheet = book.sheet_by_index(0)

# viola you have it 
# Now lets say in my excel sheet data starts with rows = 1 to 3 , and columns =0 to 2
# PS the first row are the titles

for j in range(0,4):
   for i in range(1,4):
        print("%r" %sheet.cell_value(i,j))