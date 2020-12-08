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
c_name = input("Enter Company Name: ")
noe = int(input("Enter Number of Employee: "))
profit = float(input("Enter Profit: "))

#condition
if c_id%2 != 0:
    if len(c_name) > 2:

        #condition for numebr for employee
        for i in range(2,13):
            if not noe % i ==0:
                myFun(c_id,c_name,noe,profit)
                break
