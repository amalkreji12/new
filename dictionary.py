val = {'name':'Jeep','age':'2','color':'red'}
print(val)
print(val['age'])
print(val.get('name'))

dicti={'name':'Ford',
      'age':'3',
      'color':'Green',
      'year':'2020'}

print(dicti)
print(dicti.get('age'))
print(len(dicti))

dict1={'name':'BMW',
      'age':3,
      'color':'Blue',
      'year':2020,
      'alt_color':['Green','White']
      }

print(dict1)
print(dict1.get('alt_color')[1])
print(dict1['alt_color'][0])


#using dict() inbuilt function

newdict = dict(name='BMW',color='Red',age=1,year=[2022,2023])
print(newdict)
print(newdict.get('year')[1])