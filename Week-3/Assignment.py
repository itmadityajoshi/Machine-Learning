import sqlite3
import re
import bcrypt


#database setup

conn= sqlite3.connect('users.db')
c = conn.cursor()

# creating table:

c.execute('''CREATE TABLE IF NOT EXISTS users 
          (username TEXT PRIMARY KEY, password text, email text)''')


#session management

loggedin_users = { }


# registering the new users
def register_user(username, password, email):
    if check_username(username):
        raise Exception("username is already taken.")
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise Exception("Invalid email format.")
    
    hashed_password_bytes = hash_password(password)

    c.execute("insert into users values (?,?,?)",(username, password, email))
    conn.commit()

    print(f'User {username} is registered Successfully.')



def check_username(username):
    c.execute("select * from users where username=?",(username,))
    return c.fetchone() is not None



def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def check_password(password, hashed_password):
    password_bytes = password.encode()
    hashed_password_bytes = hashed_password.encode()
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)



# user login function
def user_login(username, password):

    if username in loggedin_users:
        raise Exception('user already logged in.')
    
    c.execute("SELECT password FROM users where username=?",(username,))
    result = c.fetchone()

    # print(result)

    if result is None:
        raise Exception("invalid username.")
    
    else:
        if not check_password(password, result[0]):
            raise Exception("Invalid password.")
    
    loggedin_users[username] = True
    print('Login successfull.')



# updating the password of the existing users
def update_password(username, old_password, new_password):
    if username not in loggedin_users:
        raise Exception("User must be logged in to update the password.")
    
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()

    if result is None or not check_password(old_password, result[0]):
        raise Exception("Invalid old password.")
    hashed_new_password = hash_password(new_password)
    c.execute("UPDATE users SET password=? WHERE username=?", (hashed_new_password, username))
    conn.commit()
    print("Password updated successfully.")




# deleting the accounts
    def delete_account(username, password):
        if username not in loggedin_users:
            raise Exception("User must be logged in to delete the account.")
        c.execute("SELECT password FROM users WHERE username=?", (username,))
        result = c.fetchone()
        if result is None or not check_password(password, result[0]):
            raise Exception("Invalid credentials.")
        c.execute("DELETE FROM users WHERE username=?", (username,))
        conn.commit()
        del loggedin_users[username]
        print("Account deleted successfully.")





try:
    # register_user("madhav", "mad23", "mad123@gmail.com")
    user_login("aditya", "aditya123")
    # update_password("madhav", "mad23", "new_mad123")
    # delete_account("", "")
except Exception as e:
    print(e)


# data = c.execute('select * from users').fetchall()
# print(data)


