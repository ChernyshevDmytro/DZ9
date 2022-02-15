def input_():
    while True:
        user_command1= input('Please, give me a command:')
        
        if "hello" in user_command1 or "exit" in user_command1 or "close" in user_command1 or "good bye"  in user_command1 or "show all" in user_command1 or "phone" in user_command1  or "add" in user_command1 :
            return user_command1
        continue
        


a=input_()

print(a)