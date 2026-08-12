## input i need from the user
# total rent
# total food 
#electricity units spend
#charge per unit
 #output 
 #total amount you 've to pay is 
Number_of_person= int(input("enter the number of person="))
rent=int(input("enter your room rent="))
food=int(input( "enter your bill of food ="))
electricity_spend= int(input("enter the total of electricity spend="))
charge_per_unit=int (input("enter the charge per unit="))
total_bill= electricity_spend*charge_per_unit
output=(food+rent+total_bill)//Number_of_person
print("each person will pay=",output)