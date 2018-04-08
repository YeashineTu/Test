
import shelve
##db type could not be determined  文件已经存在，并和shelve的格式不匹配
db = shelve.open('data.txt')
db['name'] = 'tyx'
db['age'] = 24
db.close()

db = shelve.open('data.txt')
name = db['name']
print(name)



