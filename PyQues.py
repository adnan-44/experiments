#
def myFun(c_id, c_name, noe = 101, profit = 700):
    bonus = 0
    #condition for company name characters to be same
    if c_name[0] == c_name[-1]:
        bonus = (profit*5)/100
        print("same")
    else:
        bonus = (profit*15)/100

    #Display section
    print("\n\n############")
    print("Company ID :",c_id)
    print("Company Name :",c_name)
    print("Number of Employee :",noe)
    print("Profit : ",profit)
    print("Bonus :",bonus)
    print("Total Amount :",bonus+profit)

#main code
c_id = int(input("Enter Company ID: "))
if c_id%2 != 0:
    c_name = input("Enter Company Name: ")
    if len(c_name) > 2:
        #some code
        #condition for numebr for employee
        noe = int(input("Enter Number of Employee: "))
        for i in range(2,13):
            if not noe % i ==0:
                profit = float(input("Enter Profit: "))
                myFun(c_id,c_name,noe,profit)
                break
