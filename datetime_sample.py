import datetime
now=datetime.datetime.now()
print(now)
print(now.strftime('%d/%m/%y'))

print(datetime.date.today())

x=datetime.datetime(2020,5,15) #creating new date
y=datetime.datetime(2019,5,15)
diff=x-y
print(diff)




#file operation
# f=open('sample_opr.py','w') #'w' for write
# f.write("print('hello')") #writing on the file
# f.close()
#
#open file
# with open("function.py","r") as f: #used for reading a file
#     x=f.read()
# print(x)
