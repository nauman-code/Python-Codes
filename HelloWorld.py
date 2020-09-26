import os
os.system('cls')

a=int(input('Please enter first No. : '))
z=int(input('Please enter last last No. : '))
print()
for x in range(a,z):
    if(x%2!=0): continue
    print(x)
    