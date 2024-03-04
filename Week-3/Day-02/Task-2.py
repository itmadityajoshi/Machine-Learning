# importing sqlite3

import sqlite3

# connect to sqlite3 database
conn = sqlite3.connect('user_database.db')

# creating cursor object to interact with the database

cursor = conn.cursor()

'''create user table '''

# cursor.execute(''' Create table user
#                (
#                user_id INT PRIMARY KEY,
#                username Varchar(25),
#                email text(30),
#                password text(30)
#                );

#                 ''')

# conn.commit()


'''insert value on user table'''
# conn.execute('''insert into user  values (1,'aditya','adi@gmail.com','Adi@123')''')
# conn.execute('''insert into user  values (2,'adimanav','adim@gmail.com','Adim@123')''')

# conn.commit()

'''to display data of database'''
# data = cursor.execute('select * from user').fetchall()
# print(data)



'''custom expection'''
class UserError(Exception):
    pass


'''function to register new user:'''

def register_user(username, password):

    #checking if username already exist
    cursor.execute("select * from user where username",(username))
    existing_user = cursor.fetchone()

    if existing_user:
        raise UserError("Username already taken.")
    
    password_hash = password
    
    cursor.execute("insert into user (username) values ()",(username, password))
    conn.commit()


try:
    register_user("aditya")
    print("user registered successfully.")

except UserError as e:
    print("Error: ",e)

except ValueError as e:
    print("Error : ",e)


register_user('aditya', "Adi@123")