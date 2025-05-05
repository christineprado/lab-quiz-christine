
import datetime

#Declare Variables
name = "Christine Joyce Prado"
id = "231-0201"
DandT = datetime.datetime.now()

#Print
print(f"Full Name: {name}")
print(f"Student ID: {id}")
print(f"Current Date and Time: {DandT}")

#User input for issue
issue = input("Describe your networking issue: ")

#Save to network_issue.txt
with open("network_issue.txt", "w") as file:
	file.write(issue)

#Output
print("It is now saved to network_issue.txt")

