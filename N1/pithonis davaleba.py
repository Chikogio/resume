#ვეკითხებით რიცხვებს
x = int(input("პირველი რიცხვი იქნება:"))
y = int(input("მეორე რიცხვი იქნება:"))
#ვეკითხებით მათემატიკურ ფუნქციას
fun = int(input("მესამე რიცხვი იქნება:"))
#გამოთვლები
if fun > 4:
    print("რიცხვი უნდა იყოს ერთიდან ოთხამდე")
elif fun == 1:
    print(x+y)
elif fun == 2:
    print(x-y)
elif fun == 3:
    print(x*y)
elif fun == 4:
    print(x/y)
