#emails_list = ['bob@gmail.com', 'carol@gmail.com', 'eve@gmail.com']
#print(emails_list[1])
# for emails in emails_dict:
 #       emails = emails_dict.values()

#emails_dict = {
#    'Bob': 'bob@gmail.com',
#    'Carol': 'carol@gmail.com',
#    'Eve': 'eve@gmail.com'
#}


#for people in emails_dict.keys():   
#    print(f"{people}'s email is {emails_dict[people]}")


phone = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
}

output = ' '        #Initializing the variable
user_input = input('Phone: ')
for digit in user_input:        #checks the user_input for each character in the string
    if digit in phone:      #checks if the characters entered are also in the phone dictionary
        output += phone[digit] + ' '
print(output)