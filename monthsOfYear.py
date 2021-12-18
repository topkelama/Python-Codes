monthsOfYear = {
     "1st month" : "January",
     "2nd month" : "February",
     "3rd month" : "March",
     "4th month" : "April",
     "5th month" : "May",
     "6th month" : "June",
     "7th month" : "July",
     "8th month" : "August",
     "9th month" : "September",
     "10th month" : "October",
     "11th month" : "November",
     "12th month" : "December"
}
#list all months associated with the sequence number
print(monthsOfYear)
#what data type is this
print(type(monthsOfYear))
#print 5th month of the year
print(monthsOfYear["5th month"])
#print all key value pair with format 
print(monthsOfYear.items())

for i in monthsOfYear:
    print((i) + " is " +  (monthsOfYear[i]) )
    