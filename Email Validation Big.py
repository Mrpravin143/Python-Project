
email_id =input("Enter the Email:--")
k=0
j=0
d=0
if len(email_id)>=  6:
    if email_id[0].isalpha():
        if('@' in email_id) and (email_id.count('@')==1):
            if(email_id[-4]=='.') ^ (email_id[-3]=='.'):
                for i in email_id:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Wrong Email 5")
                else:
                    print("Rigth Email !")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")