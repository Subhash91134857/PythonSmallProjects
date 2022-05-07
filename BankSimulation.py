# Non-OOP

from argparse import Action


accountName = 'Subhash'
accountBalance = 100
accountPassword = '2002'

while True:
    print()
    print('Press b to get the balance')
    print("Press d to make deposite")
    print('Press w to make withdraw')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input("What do you want to do?")
    action = action.lower()
    action = action[0]

    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        if userPassword != accountPassword:
           print("Incorrect Password")
        else:
            print("Your balance is: ", accountBalance)
    elif action == 'd':
        print('Deposite:')
        userDepositeAmount = int(
            input("Please enter the amount to deposite: "))
        userPassword = input("Please enter your password:")
        if userDepositeAmount < 0:
            print("You can not deposite a negative amount:")
        elif userPassword != accountPassword:
            print('Incorrect Password!')
        else:
            accountBalance = accountBalance+userDepositeAmount
            print("Your new balance is: ", accountBalance)
    elif action == 's':
         print('Show:')
         print(' Name: ', accountName)
         print(' Balance: ', accountBalance)
         print(' Password: ', accountPassword)
         print()
    elif action=='q':
        break
    elif action=='w':
        print("Withdraw:")
        userWithdrawAmount=int(input("Please enter the amount to withdraw: "))
        userPassword=input("Please enter the password: ")
        if userWithdrawAmount<0:
            print("You can not withdraw a negative amount")
        elif userPassword!=accountPassword:
            print('Incorrect Password for this account')
        elif userWithdrawAmount>accountBalance:
            print("You can not withdraw more than you have in your current account")
        else:
            accountBalance=accountBalance-userWithdrawAmount
            print('Your new balance is: ',accountBalance)
            print('Done')