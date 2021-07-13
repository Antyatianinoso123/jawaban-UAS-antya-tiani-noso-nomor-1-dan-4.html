#!/usr/bin/env python
# coding: utf-8

# In[12]:


def conv_reamur(celcius):
    convert_reamur = 4 * celcius / 5
    return convert_reamur

def conv_farenheit(celcius):
    convert_farenheit = 9 * celcius / 5 + 32
    return convert_farenheit

def main():
    temperature = int(input('Masukan Skala Celcius: '))

    print(f'Hasil Konnversi Suhu {temperature} C adalah {conv_reamur(temperature)} Reamur')
    print(f'Hasil Konversi Suhu {temperature} C adalah {conv_farenheit(temperature)} Farenheit')

 
if __name__ =='__main__':
    main()


# In[13]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE db_film")
print("Database berhasi dibuat!")


# In[11]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
if db.is_connected():
    print("Berhasil terhubung ke database")


# In[15]:


import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = """CREATE TABLE tblfilm (
    kode_id INT AUTO_INCREMENT PRIMARY KEY,
    judulfilm VARCHAR(255),
    jenis_film varchar(255)
    
)
"""
cursor.execute(sql)
print("tabel film berhasil dibuat")
    


# In[18]:


import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor=db.cursor()
sql="INSERT INTO tblfilm (judulfilm, jenis_film)VALUES (%s, %s)"
val=("X-Men: Dark phoenix", "Action")
cursor.execute(sql, val)

db.commit()
print("{} data ditambahkan".format(cursor.rowcount))


# In[20]:


import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql= "INSERT INTO tblfilm (judulfilm, jenis_film) VALUES (%s, %s)"
values= [
    ("Aladdin", "fantasy"),
    ("Godzilla II: king of monsters","fantasy"),
    ("john wick: chapter 3 - parabellum","Action")
]
for val in values:
    cursor.execute(sql, val)
    db.commit()
    
print("{} data ditambahkan".format(len(values)))


# In[21]:


import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql= "SELECT * FROM tblfilm"
cursor.execute(sql)
results = cursor.fetchall()

for data in results:
    print(data)


# In[23]:


import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql= "SELECT * FROM tblfilm"
cursor.execute(sql)

results = cursor.fetchone()

for data in results:
    print(data)


# In[27]:


import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor = db.cursor()
sql= "UPDATE tblfilm SET judulfilm=%s, jenis_film=%s WHERE kode_id=%s"
val=("X-Men: Dark phoenix", "Fantasy Action", 1)

cursor.execute(sql, val)

db.commit()

print("{} data diubah".format(cursor.rowcount))


# In[30]:


import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor=db.cursor()
sql= "DELETE FROM tblfilm WHERE kode_id=%s"
val=(1, )
cursor.execute(sql,val)

db.commit()
print("{} data dihapus".format(cursor.rowcount))


# In[ ]:




