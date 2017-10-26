with open(r'email.csv','r', encoding='utf-8') as input_file:
   with open(r'students_processed.csv','w', encoding='utf-8') as output_file:
       for x in input_file:
           stripped_line = x.strip()
           str_list = stripped_line.split(';')
           name = str_list[0]
           email = str_list[1]
           output_file.write('Hi, 'f'{name}! We\'ve sent an email to {email} \n')
