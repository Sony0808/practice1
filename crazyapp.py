def person(**data):
    for k, v in data.items():
        if k == 'firstname':
            print(k,' :', v)
        elif v == 'lastname':
            print(k,'   :', v)

        elif k =='age':
            print(k, '   :', v)
        else:
            print(k,':', v)


fname = input("Enter your firstname :")
lname = input("Enter your lastname  :")
age = input("Enter your age       :")
mobile = input("Enter your mobile no :")
print('')


person(firstname= fname,lastname=lname,age=age,mobileno = mobile)

input()


