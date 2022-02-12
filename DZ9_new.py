

#contact_book.get(telef)
contact_book={"ff":45454, "dd":6766,}
#name1=''
#telef=9999
#contact_book=dict()


def input_error (func):
    def inner(user_command1):
        a=0  
        while a<2:
            try:         
                name1, telef, command1=func(user_command1)
                a+=1
            except TypeError:         
                print("Give me name and phone please")
                user_command1=input_ ()
                name1, telef, command1=func(user_command1)


            except  IndexError:
                print("Give me true name or phone please")
                user_command1=input_ ()
                name1, telef, command1=func(user_command1)

            except  ValueError:
                print("Give me true name or phone please")
                user_command1=input_ ()
                name1, telef, command1=func(user_command1)

            except  KeyError:
                print("Give me true name or phone please")
                user_command1=input_ ()
                name1, telef, command1=func(user_command1)







        return name1, telef, command1    
    return inner    


def input_ ():
    user_command1= input('Please, give me a command1:')
    return user_command1

@input_error
def parser(user_command1_norm):
    if user_command1_norm in ["hello", "exit", "close", "good bye", "show all"]:
        command1=user_command1_norm
        return "", "", command1
    elif 'phone' in user_command1_norm:
        b=user_command1_norm.split('phone ')
        name1=b[-1]
        command1='phone'
          
        #print('phone2222')
        return name1,"", command1
    
    elif 'add' in user_command1_norm or 'change' in user_command1_norm:
        c=user_command1_norm.split(' ')
        #with open (aa, 'a') as fh:
            #fh.write
        name1=c[1]
        telef=c[2]
        command1=c[0]
        #print(c)
        #print(f'com {command1}')
        #print(f'name {name1}')
        #print(f'tel {telef}')
        return name1, telef, command1    
    
    

def normalization (user_command1):
    user_command1.casefold()   
    user_command1_norm=user_command1
    return user_command1_norm





def main ():


    def close_func(): 
        print('Good bye!')
            

    def show_func():
        print(contact_book)
    
    def phone_func():
        print(f'{name1} phone is')
        print(contact_book.get(name1))

    def change_func():
        #print('gbf')
        #print(f'name {name1}')
        #print(f'tel {telef}')
        contact_book[name1] = telef
        #print(contact_book)
         

    def hello_func():    
        print('How can I help you?')

    command1S = {
    'good bye': close_func,
    'close': close_func,
    'exit': close_func,
    'show all': show_func,
    'phone': phone_func,
    'change': change_func,
    'add': change_func,
    'hello': hello_func
}


       

    
    def get_handler(command1):
        return command1S[command1]


        
     



    while True:    
        user_command1= input_ ()

        if user_command1 in ['close', 'good bye', 'exit']:       
            close_func()
            break
        user_command1_norm=normalization (user_command1)
        
        name1, telef, command1 = parser(user_command1_norm)

        #get_handler(command1)
        #print(f'com {command1}')
        #print(f'name {name1}')
        #print(f'tel {telef}')
        #print(f'{contact_book.get(name1)}')

        a= get_handler(command1)
        a()




        
          

main ()


        
