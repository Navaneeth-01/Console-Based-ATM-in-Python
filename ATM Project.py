print("**********************")
print("Welcome to ATM")
print("**********************")
print()
accounts = {
    1001 : ["Ram","24-08-2000",35500,5464],
    1002 : ["Sai","16-07-1998",15400,2486],
    1003 : ["Teja","20-01-1995",40000,None],
    1004 : ["Kumar","01-05-2001",55000,4567]
    }
dobm = {1:"January",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
while True:
    print("Choose Your Option")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Pin Generation")
    print("4. Mini statement")
    print("5. Change pin")
    print("6. Services")
    print("7. Exit")
    option = int(input("Enter Your Option: "))
    print()
    if option == 1:
        print("**********************")
        accno =  int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exist !")
        else:
            pin = int(input("Enter Pin: "))
            if accounts[accno][-1] == None:
                print("Generate Pin")
            else:
                if accounts[accno][-1] != pin:
                    print("Invalid Pin")
                else:
                    amt = int(input("Enter Amount to Withdraw: "))
                    if amt > accounts[accno][-2]:
                        print("Insufficent Funds ")
                    else:
                        print("Withdraw Sucessfull !")
                        accounts[accno][-2] -= amt
        print("**********************")
    elif option == 2:
        print("**********************")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account does not Exist")
        else:
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][-1]:
                print("Invalid Pin")
            else:
                amt = int(input("Enter Amount to Deposit: "))
                accounts[accno][-2] += amt
                print("Deposit Sucessfull")
        print("**********************")
    elif option == 3:
        print("**********************")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exists")
        else:
            if accounts[accno][-1] == None:
                pin = int(input("Enter Pin: "))
                cpin = int(input("Confirm Pin: "))
                if pin != cpin:
                    print("Pin Does not Match")
                else:
                    accounts[accno][-1] = pin
                    print("Pin Generated Sucessfully")
            else:
                print("Pin Already Exist")
        print("**********************")
    elif option == 4:
        print("**********************")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exists")
        else:
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][-1]:
                print("Invalid Pin")
            else:
                print(f"Name: {accounts[accno][0]}")
                print(f"Account Number: {accno}")
                dob = accounts[accno][1].split("-")
                date = dob[0]
                month = dobm[int(dob[1])]
                year = dob[2]
                dob = date + "-" + month + "-" + year
                print(f"Date of Birth: {dob}")
                print(f"Account Balance: {accounts[accno][-2]}")
        print("**********************")
    elif option == 5:
        print("**********************")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exists")
        else:
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][-1]:
                print("Invalid Pin")
            else:
                new_pin = int(input("new pin: "))
                conform_pin = int(input("conform new pin: "))
                if new_pin != conform_pin:
                    print("pin not matched")
                else:
                    accounts[accno][-1] = conform_pin
                    print("pin change succesfully")
        print("**********************")
    elif option == 6:
        print("**********************")
        accno = int(input("Enter Account Number: "))
        print("1. Bill Payments")
        print("2. Fund Transfer")
        option = int(input("Enter Your Option: "))
        print()
        if option == 1:
            print("Bill Payments")
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][-1]:
                print("Invalid Pin")
            else:
                amt = int(input("Enter Amount: "))
                print("Bill Payment Successfully Completed")
        elif option == 2:
            print("Fund Transfer")
            to_accno = int(input("Enter Account: "))
            if to_accno not in accounts:
                print("Account Does not Exist")
            else:
                pin = int(input("Enter Pin: "))
                if pin != accounts[accno][-1]:
                    print("Invalid Pin")
                else:
                    amt = int(input("Enter Amount: "))
                    print("Fund Transfered Successfully")
        print("**********************")
    else:
        break
        print("Thank You For Visiting")
