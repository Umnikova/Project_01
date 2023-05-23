import sqlite3

connection = sqlite3.connect('teachers (4).db')


        
        # создание таблицы
#sqlquery =  """ CREATE TABLE Students(
#Student_ID INTEGER NOT NULL,
#Student_Name TEXT NOT NULL,
#School_ID INTEGER NOT NULL PRIMARY KEY
#);"""



        # Наполнение таблицы
#sqlquery ="""INSERT or IGNORE INTO Students (Student_ID, Student_Name, School_Id)
#VALUES
#('201', 'Иван', '1'),
#('202', 'Петр', '2'),
#('203', 'Анастасия', '3'),
#('201', 'Игорь', '4');
#"""

def get_connection():
  connection = sqlite3.connect('teachers (4).db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()


        # Создание функции и запроса
def getinfo_school_and_student(Student_Id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = """SELECT Students.School_Id, Students.Student_ID,Students.Student_Name, School.School_Name FROM Students FULL JOIN School ON Students.School_Id=School.School_Id WHERE Student_Id=?;"""
    cursor.execute(sqlquery, (Student_Id,))
    records = cursor.fetchall()
    print("Данные о школе и студенте по Id: ", Student_Id, '\n')
    for row in records:
      print ("ID школы: ", row[0])
      print ("ID студента: ", row[1])
      print ("Имя студента: ", row[2])
      print ("Название школы: ", row[3])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных ", error)

getinfo_school_and_student(204)





   