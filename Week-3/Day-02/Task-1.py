class Error(Exception):
    pass

class DobExcepetin(Error):
    pass

user_age = int(input('enter your valid age : '))

try:
    if user_age <= 30 and user_age >= 20:
      print('You are valid for program.')

    else:
        raise DobExcepetin
except DobExcepetin:
    print('sorry, please pass the valid age.')
40