##random_password_generator
import random
import csv
import os
print("************Welcome to Random Password Generator************")
print()
num_list=['0','1','2','3','4','5','6','7','8','9']
spcl_list=['!','@','#','$','%','&','*','+','=','/','|']
lowcase_list=['a','b','c','d','e','f',
              'g','h','i','j','k','l','m','n',
              'o','p','q','r','s','t','u','v','w','x','y','z']
upcase_list=['A','B','C','D','E','F','G','H','I','J',
             'K','L','M','N','O','P','Q','R','S','T','U','V',
             'W','X','Y','Z']

full_list=num_list+spcl_list+lowcase_list+upcase_list
#taking one random from each list
num=random.choice(num_list)
spcl=random.choice(spcl_list)
lowcase=random.choice(lowcase_list)
upcase=random.choice(upcase_list)

#combining all of them to make initial password so all req. covered

initial_pass=num+spcl+lowcase+upcase
print("Please enter the svcaccount associated")
account=input()
for i in range(0,10):
    initial_pass=initial_pass+random.choice(full_list)
print("Your desired password is:::::::::",     initial_pass)

#csv file code starts
#storing info in csv_file
#columns=['Account','Password']
#csv_dict={'Account':account,'Password':initial_pass}

#writing to csv file
#check if file already exists
file_exists=os.path.isfile('storage.csv')

with open('storage.csv','a',newline='') as f:
    headers=['Account','Password']
    writer=csv.DictWriter(f,fieldnames=headers)
    if not file_exists:
        writer.writeheader()
    writer.writerow({'Account':account,'Password':initial_pass})
    
