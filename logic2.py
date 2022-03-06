x=int(input("Enter your choice:")) #Let n be the choice i.e. a,b,c,d
if x>0:
    if x<10:
        print("Keep up the good work, everything is normal.Keep shining")
    elif x<20:
        print("This is common, try to normalise things. Hope for the best, the good is yet to come")
    elif x<30:
        print("The situation is under control. Mild therapy required. Try talking with yor family members and friends. Try meditation and yoga to keep your mental health stable and balanced")
    elif x<40:
        print("The situation is getting out of control, immediate requirement of consultation.")
    elif x<50:
        print("Consult a Psychatrist and Get your hormonal balance checked")
    elif x<55:
        print("Immediate requirement of Psychaitrist, The situation is getting out of hand")
    elif x<60:
        print("You might have reached chronic depression, Try to consult a neurologist or a psychatrist and take regular medicines")
    else:
        print("inappropriate option")
else:
    print("Over scored")