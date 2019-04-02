import pyodbc
import pickle
import os
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=aisdl;UID=sa;PWD=123456')
cursor = cnxn.cursor()
cursor.execute("EXECUTE [dbo].[PyPlotMatplotlib]")
tables = cursor.fetchall()
for i in range(0, len(tables)):
    fig = pickle.loads(tables[i][0])
    fig.savefig(str(i)+'.png')
print("The plots are saved in directory: ",os.getcwd())
