

input_file = open('geckodriver.log')
a=0
new=[]

for line in input_file:
    a += 1
    new.append(str(a)+': '+line.rstrip())

input_file.close()

new_file = open('newdriver.txt','w')
for i in new:
    new_file.write(i+'\n')

new_file.close()



