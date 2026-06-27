user_input = ''

#print('start -- start car')
#print('stop -- stop car')
#print('quit -- exit game')
IsStarted = True

while user_input !=  'quit':
    user_input = input('> ').lower()

    if user_input == 'start':
        if IsStarted:
            print('Car already started!')
        else:
            IsStarted = True
            print('Car started...Ready to go!')
 
    elif user_input =='stop':
        if not IsStarted:
            print('Car alreasdy stopped!')
        else:
            IsStarted = False
            print('Car stopped!')
    elif user_input == 'help':

        
        print('''
start -- start car
stop -- stop car
quit -- exit game
              ''')
    elif user_input == 'quit':
        break
    elif user_input != 'quit' or 'start' or 'stop':
        print('Sorry, I do not understand that.')
    
       