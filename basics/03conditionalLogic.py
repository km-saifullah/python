# basic logic
marks = 35
if marks > 40:
    print('Pass')
else: 
    print('Fail')

age = float(input("Enter age: "))
if age>=18:
    print('Eligable for vote')
else:
    print('Not eligable for vote')


# if-elif

mark =  int(input("Enter Your Marks: "))
if mark>=80:
    print('GPA: A')
elif mark >=70:
    print('GPA: B')
elif mark >=60:
    print('GPA: C')
elif mark >=50:
    print('GPA: D')
else:
    print('GPA: F')


light = input('Enter your traffic light color: ')
if light == 'yellow':
    print('You need to wait for a while')
elif light == 'red':
    print('your car must need to stop')
elif light == 'green':
    print('You can go')
else:
    print('Wrong Input')

