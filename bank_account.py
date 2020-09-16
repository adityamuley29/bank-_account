if __name__ == "__main__":
    net_amount=0
    while(True):
    
        person = input("Enter the amount that you want to Deposit/Withdral ? ")
        transaction = person.split(" ")
        type = transaction[0]
        amount =int( transaction[1])
        if type =="D" or type =='d':
                net_amount += amount
                print("Your Net_amount is :-",net_amount)
        elif type == 'W' or 'w':
            net_amount -= amount 
            if net_amount>0:
                print("Your Net_amount is :-",net_amount)
            else:
                print("Insufficient Balance!!!!!!!")
        else:
            pass

        ext = input("Want to Continue (Y for yes and N for no)")
        if  not (ext=='Y' or ext=='y'):
            break
    