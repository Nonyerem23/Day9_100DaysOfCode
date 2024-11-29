


print("GENERATION IDENTIFIER")
print()
name = input("What's your name?:")
print("Hey", name, "you're going to identify the Generation you belong to, then you'll thank me later!")
print("So you'll have to patiently type in your year of birth to see the generation you belong to.")
print()
yearofbirth = int(input("Which year were born?:"))
if yearofbirth  <= 1900:
    print("You belong to Lost Generation")

elif  yearofbirth <= 1927 :
   print("Wonderful, you togreatest generation")
elif yearofbirth <= 1945 :
    print("You're in Silent generation") 
elif yearofbirth <= 1964 :
    print("You're in Baby generation")
elif yearofbirth <= 1980 :
    print("You're in Generation X")
elif yearofbirth <= 1996 :
    print("You're in Millennials generation")
elif yearofbirth <= 2012 :
    print("Hey!", name, "I know you're aware of where you belong, but I just want to remind you though, lol.\nYou're part of the GEN Z")
elif yearofbirth >= 2013 and yearofbirth < 2040 :
    print("GEN ALPHA")
else:
    print("Some went wrong")