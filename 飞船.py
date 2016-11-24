import time
shipname="zhangyonghao"
captain="zhangyong"
location="china"
password="liyujie"
pattempt=raw_input("enter the password")
while pattempt!=password:
    print"password incorrect"
    pattempt=raw_input("enter the password")
print"password correct!welcome to the"+shipname+"."
print""
print"the spaceship"+shipname+"is here waiting for you--"+captain+"!"
choice=""
while choice!="/exit":
    print"what would you like to do?"+captain+"?"
    print""
    print"a.travel to amother planet"
    print"b.fire cannons"
    print"c.open the airlock"
    print"d.just have a rest"
    print"/exit to exic"
    print""
    choice=raw_input("enter your choice:  ")
    if choice=="a":
        destination=raw_input("where would you like to go?")
        print"leaving"+location
        print"travelling to "+destination
        time.sleep(5)
        print"arrived at "+destination
        location=destination
    elif choice=="b":
        print"firingcannons"
        time.sleep(1)
        print"bang"
        time.sleep(3)
    elif choice=="c":
        print"opening airclock"
        time.sleep(3)
        print"airlock open"
        time.sleep(3)
    elif choice=="d":
        confirm=raw_input("are you sure to just have a rest?")
        if confirm=="yes":
            print"ship will have a rest"
            print"3"
            time.sleep(1)
            print"2"
            time.sleep(1)
            print"1"
            time.sleep(1)
            print"goodbey!boom"
            choice="/exit"
    elif choice=="/exit":
        print"goodbye"
    else:
        print"invalid input.please select a,b,c or d./nexit to exit"

