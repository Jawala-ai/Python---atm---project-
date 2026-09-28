balance = 10000
pin = 1234
transcations = []
user_pin = int(input("enter a pin"))
if user_pin == pin:
    print("pin correct")
while True:
    print("1.check money")
    print("2.deposite money")
    print("3.withdraw money")
    print("4.transcation history: " )
    print("5.exit")
    choice = int(input("choose an option:"))
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a number")
        continue
    
    
    if choice == 1:
        print("your balance is",balance)
    elif choice == 2:
        amount = int(input("enter deposite amount:"))
        balance = balance + amount
        transcations.append("deposited:"+ str(amount))
        print("new balance is",balance)
    elif choice == 3:
        amount = int(input("enter withdraw amount"))
        if amount <= balance:
           balance = balance - amount
           print("new balance is",balance)
        else:
           print("insufficient balance")
      
    elif choice == 4:
        print("transcation history")
        if len(transcations) == 0:
           print("no transcation")
        else:
           for transcation in transcations:
              print(transcations)
    elif choice == 5:
        print("goodbye.thankyou")
    else:
      print("invalid option")
else:
  print("wrong PIN")


           



