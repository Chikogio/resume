i = 2
inete = [1,1]
while i <=501:
    inete.append(inete[i-2]+inete[i-1])
    i+=1

didWePrintYES = False
y = 8

for x in inete: 
    if y==x:
        print("yes")
        didWePrintYES = True


if didWePrintYES == False:
    print  ("no")   
    
    
