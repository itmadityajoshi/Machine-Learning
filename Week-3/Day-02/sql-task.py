import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

# conn.execute('''create table user (
#                username varchar(30),
#                password varchar(30),
#                email varchar(50)
# )''')

# conn.commit()


# conn.execute("insert into user values ('aditya', 'Adi@123', 'adi@gmail.com')")
# conn.execute("insert into user values ('Madhav', 'Mad@123', 'mad@gmail.com')")
# conn.execute("insert into user values ('Sajan', 'Saj@123', 'saj@gmail.com')")


# conn.commit()

# show = cursor.execute("select * from user").fetchall()
# print(show)






class Error(Exception):
    pass

class UserError(Error):
    pass

def register_user(username, password, email):
    cursor.execute("select * from user where username=?",(username,))
    existing_user = cursor.fetchone()

    if existing_user:
        raise UserError("user already taken.")
    

    password_hash = password

    '''insert value into the database'''
    cursor.execute("insert into user value (?,?,?)",(username, password_hash, email))
    conn.commit()

try:
    user_name = input("enter the name.")
    user_pass = input('enter the password. ')
    user_email = input('enter the email. ')

    query = "insert into user (username, password, email) values(?,?,?)", (user_name, user_pass, user_email)
    cursor.execute(query,(user_name, user_pass, user_email,))
    conn.commit()

except UserError as e:
    print("error : ",e)



register_user(user_name, user_pass, user_email)




# def register_user():
#     user_name = input("enter the name: ")
#     user_pass = input("enter the password: ")
#     user_email = input("enter the email: ")

#     try:
#         if user_name != '' and user_pass != '':
#           cursor.execute('select username from user where username=?',(user_name,))
        
#           if cursor.fetchone() is not None:
#             raise UserError
#           else:
#             hash_password = user_pass
#             email = user_email
#             cursor.execute('insert into user values (?,?,?)',(user_name, hash_password, email))
#             conn.commit()
#         else:
#           raise UserError

#     except UserError:
#        print("Error : Enter valid data.")
# # register_user()
        



