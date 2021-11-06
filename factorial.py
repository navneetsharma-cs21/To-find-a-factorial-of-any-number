a = int(input('enter the value of a '))
factorial = 1
if a<0:
  print ( 'sorry factorial of negative number does not exist');
elif a==1 or a==0:
    print('factorial is',1);
else:
    for i in range (1,a+1):
        factorial = factorial * i;
print(f"factorial of your value is {factorial}");
