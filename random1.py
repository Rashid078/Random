from __future__ import division
import time
#It generates Random number between 0-99

def round_off(x):              #Just to round off the values for 27% and 73%
    i, f = divmod(x, 1)
    return int(i + ((f >= 0.5) if (x > 0) else (f > 0.5)))

		
while True:                     #For taking input from user that how many total random number they want
	try:
		total_num = int(input("How many times you want to generate random number "))
		break
	except:
		print("That's not a Integer")

mid = (99-0)/2                  #Deduce mid point of the range to decide its 27% and 73%
min27 = (27/100)*total_num       #Here deducing 27% of total random number needed
min27 = round_off(min27)         #Rounding off the value  
max73 = (73/100)*total_num       #Here deducing 73% of total random number needed
max73 = round_off(max73)         #Rounding off the value 
count = 0                        #count for lower number
count1 = 0                       #count for higher number
random_number = []               #Final desired random numbers
c=1
print min27
print max73

#Main logic where the random number is generated and checked if it is a higher or lower number in the range and accordingly the count is updated
while count <= min27 and count1 <= max73:
	t = time.time()
	num=int(str(t-int(t))[2:])%100   #Generating Random numbers and checking later that its a high or low value in the range
	if num >= mid and count1 <= max73:
		random_number.append(num) #Push the generated value to a list if it is a high value in the range
		count1 += 1               #Incrementing the count1 for 73%
	if num < mid and count <= min27:
		random_number.append(num) #Push the generated value to a list if it is a low value in the range
		count += 1                #Incrementing the count for 27%
print random_number


