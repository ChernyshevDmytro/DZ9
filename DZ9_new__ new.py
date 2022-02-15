

#contact_book.get(telef)
contact_book={"ff":45454, "dd":6766,}

def input_error (get_handler):
    def inner(command1):
        try:
            get_handler(command1)
            return  get_handler(command1) 
        except ValueError as e:
            print(e)
            command1 ='help'
        except IndexError as e:
            print(e)  
            command1 ='help' 
        except TypeError as e:
            print(e) 
            command1 ='help'
        except KeyError as e:
            print("hhhhhh")
            command1 ='help'             
        return command1 , print(command1)         
    return inner    

def input_():
    while True:
        user_command1= input('Please, give me a command:')
        
        if "hello" in user_command1 or "exit" in user_command1 or "close" in user_command1 or "good bye"  in user_command1 or "show all" in user_command1 or "phone" in user_command1  or "add" in user_command1 or "change" in user_command1:
            return user_command1
        continue 



def normalization (user_command1):
    user_command1.casefold()   
    user_command1_norm=user_command1
    return user_command1_norm    

def input_error_2 (parser):
    def inner(user_command1_norm):
        a=0  
        while a<10:
            try:         
                name1, telef, command1 = parser(user_command1_norm)
                a+=1
                return name1, telef, command1
            except TypeError:         
                print("Give me name and phone please")
                #return input_()              

            except  IndexError:
                print("Give me true name or phone please")
                name1= input('Please, give me a name:')
                telef= input('Please, give me a telefone:')
                command1 = "add"
                return name1, telef, command1
                

            except  ValueError:
                print("Give me true name or phone please")
                #return input_()                

            except  KeyError:
                print("Give me true name or phone please")
                #return input_()
    return inner         

def help_func():
    user_command1= input('Please, give me a new command1:')
    user_command1_norm=normalization (user_command1)        
    name1, telef, command1 = parser(user_command1_norm)
    
    return name1, telef, command1 

@input_error_2
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
    else:  
        
        name1=''
        telef=""
        command1="help"
        return name1, telef, command1

       

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
    'hello': hello_func,
    'help': help_func,
}


       

    @input_error   
    def get_handler(command1):
        return command1S[command1]


    
    while True:    
        user_command1= input_()

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
        if command1 is not None:
            a= get_handler(command1)
            a()
      
          
if __name__ =="__main__":
    main ()

     
