def first(msg):
	print(msg)
	first("Hello everybody")
	second = first
	second("hey guy")
	print(second) 

def inc(x):
	return x + 1 
def dec(x):
	return x - 1
def operate(func, x):
	result = func(x)
	return result
print(operate(inc, 5))
print(operate(dec, 3))
print(operate(inc, 4))
def is_return():
	print("Hello")
	return is_return
	new = is_call
#new()
base = 6
height = 4
area = (base*height)/2
print("the area of the triangle is: ", int(area))
def greet(name, departement):
	print("Hello", name)
	print("You are part of:", departement)
	greet("Alpha", "Technology")
def area_triangle(base, height):
	return (base*height)/2
	print(area_triangle(2,4))
	area_a = area_triangle(5, 10)
	area_b = area_triangle(4,4)
	area_sum = area_a + area_b
	print("The area of A is: ",area_a)
	print("The area of B is: ", area_b)
	print("The sum of the two areas is:", int(area_sum))
def get_seconds(hours, minutes, seconds):
	print(hours, "H",minutes ,"m",seconds,"s", 'equal:')
	return 3600*hours + 60*minutes + seconds
	amount_a = get_seconds(2,30,20)
	print(amount_a, "s")
	name = "Bamoye"
	number = len(name)*7
	print("Hello", name, "Your favorite number is:", number)

def month_days(month, days):
	return month, "has", str(days), "days"
	print(month_days("june", 30))
	print(month_days("july", 31))
def month_of_day(month, day):
	june_day = 30
	print("june has", june_day, "days today have an excellent day my dude.")
	july_day = 31
	print("july has", july_day, "days today have a great day.")
	month_of_day("june", 30)
def calculate(x):
	a = 5
	b = (a*x)**2
	print(b)
	calculate(2)
def circle_area(radius):
	pi = 3.14
	area = pi*(radius**2)
	print(area)
	rounded = round(area)
	print(rounded)
	circle_area(5)
def rectangle_area(base, height):
	area = base*height
	print("The area of rectangle is", str(area))
rectangle_area(5,8)
def num_order(num1, num2):
	if num1 > num2:
		return num2, num1
	else:
		return num1, num2
smaller, bigger = num_order(75, 70)
	print(smaller, bigger)
def greeting(name):
	if name == "paul":
		print("Welcome back", name)
	else:
		print("Hello", name)
greeting("paul")
greeting("jean")
def exam_grade(score):
	if score>95:
		grade = "Top Score"
	elif score>=60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail
def sum(x, y):
	return(x+y)
	print(sum(sum(1,2), sum(3,4)))


def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
			word = word1
	elif len(word2) >= len(word1) and len(word2)>= len(word3):
			word = word2
	else:
		word = word3
		return(word)

	print(longest_word("chair", "couch", "table"))
	print(longest_word("bed", "bath", "beyond"))
	print(longest_word("laptop", "notebook", "desktop"))

def fractional_part(numerator, denominator):
	if numerator > 0 and denominator > 0:
		return numerator % denominator  # Operate with numerator and denominator to 
	else:
			# keep just the fractional part of the quotient
			return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
		return hex_color
	elif color == "green":
		hex_color = "#00ff00"
		return hex_color
	elif color == "blue":
		hex_color = "#0000ff"
		return hex_color
	else:
		hex_color = "unknown"
		return hex_color

		return ""

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


def format_name(first_name, last_name):
  string = (last_name, first_name) # code goes here
  if string == ("", first_name):
  	print("name:", first_name)
  elif string == (last_name, ""):
  	print("name:", last_name)
  elif string == ("", ""):
  	print("")
  else:
  	print("name:", last_name, first_name)
  	return string 

  	print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string


def fractional_part(numerator, denominator):
# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
if denominator == 0 or numerator == 0:


	fraction = 0       #to solve if denominator or numerator is 0
	print("0")
else:

	fraction = numerator / denominator
	while fraction > 1:
		fraction = fraction - 1
		return fraction

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0000ff
x = 0
while x < 5:
	print("not yet x = ", str(x))
	x += 1
	print("It is ok now x = ", str(x))


def count_down(number):
	current = 5
	while current > 0:
		print(current)
		current -= 1
		print("Zero!")
	count_down(5)


def print_range(start, end):
	n = 1
	while n <= end:
		print(n)
		n+=1
	print_range(1,5)
	print("you are done!")

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:

  # Check if factor is a divisor of number
  if number % factor == 0:
	# If it is, print it and divide the original number
	print(factor)
	number /= factor
else:
	# If it's not, increment the factor by one
	factor += 1
	return "Done"

	print_prime_factors(200)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT


def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  if n == 0:
  	return False

  	while n % 2 == 0:
  		
  		n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
  	return True 
  	return False

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
print(is_power_of_two(4)) # Should be True
print(is_power_of_two(11)) # Should be False
'''
def sum_divisors(n):
  sum = 0
  # Return the sum of all divisors of n, not including n

  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
'''

import math 
def sum_divisors(num) : 

  # Final result of summation of divisors 
  result = 0

  # find all divisors which divides 'num' 
  i = 2
  while i<= (math.sqrt(num)) : 

	# if 'i' is divisor of 'num' 
	if (num % i == 0) : 

	  # if both divisors are same then 
	  # add it only once else add both 
	  if (i == (num / i)) : 
	  	result = result + i; 
	  else : 
	  	result = result +  (i + num//i); 
	  	i = i + 1

  # Add 1 to the result as 1 is also  
  # a divisor 
  return (result + 1); 


  print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

print(int(math.sqrt(45)))



import math 

# Function to calculate sum of all proper 
# divisors num --> given natural number 
def sum_divisors(num) : 
	
  # Final result of summation of divisors 
  if num == 0:
  	return 0
  else:

  	result = 0
  	
  # find all divisors which divides 'num' 
  i = 2
  while i<= (math.sqrt(num)): 
  	
	# if 'i' is divisor of 'num' 
	if (num % i == 0) : 
		
	  # if both divisors are same then 
	  # add it only once else add both 
	  if (i == (num / i)) : 
	  	result = result + i; 
	  else: 
	  	result = result +  (i + num/i); 
	  	i = i + 1
	  	
  # Add 1 to the result as 1 is also  
  # a divisor
  hell = int(result + 1)
  return hell

  print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114




import math
def sum_divisors(n):
	
	if n == 0:
		return 0
	else:
		result = 0
		i = 2
		while i <= (math.sqrt(n)):

			if (n % i == 0):

				if (i == (n / i)):

					result += i;
				else:
					result = result + (i + n / i); 
					i += 1
					hell = int(result + 1)
  # Return the sum of all divisors of n, not including n
  return hell

  print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

def multiplication_table(number):
  # Initialize the starting point of the multiplication table
  multiplier = 1
  # Only want to loop through 5
  while multiplier <= 5:
  	result = number*multiplier
	# What is the additional condition to exit out of the loop?
	if result==25 :
		break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
	# Increment the variable for the loop
	multiplier += 1

	multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8) 
# Should print: 8x1=8 8x2=16 8x3=24

product = 1
for n in range(1,10):
	product*=n
	print(product)
	print(math.factorial(4))
	print(int(math.sqrt(81)))

	def to_celsuis(z):
		return (x - 32)*5/9
		for x in range(0,101,5):
			print(x,':',to_celsuis(x))
			for left in range(7):
				for right in range(left, 7):
					print("[" + str(left) + "|" + str(right) + "]", end=" ")
  #print()

  print("welcome", end = " ")
  print("Alpha", end = " ")
  print()
  team_list = ['Barcelona', 'Real Madrid', 'Liverpool']
  for team in team_list:
  	for xteam in team_list:
  		if xteam != team:
  			print(team, 'vs', xteam)
	#print(esp_team)
	for x in range(0, 26, 5):
		print(x)
#import math
print(math.factorial(10))

'''

from spellchecker import SpellChecker

corrector = SpellChecker()
word = input("Enter a word:")
correct_word = corrector.correction(word)
if word in corrector:
  print("correct")
print("The correct word is: ", correct_word)

'''
def hello_friend(friends):
	for friend in friends:
		print("Hi", friend)
		print(hello_friend(["Moussa", "Mohamed", "Alou", "Lassi"]))
'''
def valid_user():


  is_valid = ["Neymar", "Messi", "CR7", "Alpha"]
  fcb = input("Enter footballer name:")
  #for user in is_valid:
  if fcb in is_valid:
	  print(fcb, "is valid!" )
  else:
	  print(fcb, "Is not part of the team")
valid_user()

'''
def multiple(x):
	for n in range(100):
		n = n*x
		if n <= 100:
			print(n)
			print(multiple(7))

def sum_positive_numbers(number):
	positive_sum = 0
				
	for x in range(1, number+1):
					
		positive_sum +=x

	return positive_sum

					

print(sum_positive_numbers(8)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15



#using normal functions
def sum_positive_numbers(n):
	sums = 0
	for v in range(1,n+1):
		sums += v
		return sums

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


"""
def count_users(group):
  count = 0
  for member in get_members(group):
  count += 1
  if is_group(member):
	count += count_users(member)-1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18


num = 10
for x in range(1, 11):
  print(num, "x", x, "=", num*x)

number = int(input("Enter the number to see the multiplication table >"))
for i in range(1,11):
  print("The multiplication table of", number, "is:", number, "x", i, "=", number*i)



number = int(input("Enter a number to multiply >"))
x = 1
while x <=10:
  print("The multiplication table of",number, "is:", number, "x", x, "=", number*x)
  x+=1

  """

  for x in reversed(range(11)):
  	print(x)


def count(start, stop):
  	x = start
  	if x < stop:
  		return_string = "counting up: "
  	while x <= stop:
  		return_string += str(x)
  	if x < stop:
  		return_string += " "
  		x+=1
  	else:
  		return_string = "counting down: "
  	while  x >= stop:
  		return_string += str(x)
  	if x > stop:
  		return_string += " "
  		x-=1
  		return return_string

  	print(count(1, 10))
  	print(count(8, 2))
  	print(count(4, 4))


  							for x in range(0 , 10+1, 2):
  								print(x)

  								for left in range(7):
  									for right in range(1,7):
  										print("[" + str(left) + "|" + str(right) + "]", end = "   ")
  										print()


  										name = "Bamoye TRAORE"
  										print(name[1])
  										print(name[-1])
  										print(name[-2])
  										print(name[-3])
  										print(len(name))
  										color = "Orange"
  										print(color[1:5])
  										fruit = "pineapple"
  										print(fruit[4:])
  										print(fruit[:4])

  										message = "Akon is favorite artist"
  										new_message = message[0:7] + " my " + message[8:]
  										print(new_message)
  										pet = "dog and cat"
  										print(pet.index("n"))
  										print(pet.index("cat"))
  										print(pet.index("t"))
  										print("horse" in pet)
  										print("cat" in pet)
  										print(pet.upper())
  										print("Dragon" in pet)
  										print("apple" in pet)
  										print("dog" in pet)
  										print(pet.lower())
  										answer = " yes "
  										print(answer.strip())
  										name = "Bamoye TRAORE"
  										print(name.count("R"))
  										string = "Alpha is getting stronger for days on end"
  										print(string.endswith("en"))
  										print(string.endswith("end"))
  										print(string.startswith("end"))
  										print(string.startswith("A"))
  										print(name)
  										print(name.isnumeric())
  										number = "123456789"
  										print(number.isnumeric())
  										print(name.isalpha())
  										print(number.isalnum())
  										print(int("222") * int("333"))
  										background = "Alpha is profesionnal a programmer"
  										print("-".join(background))
  										new_name = "alpha Traore"
  										print(new_name.capitalize())



  										def initials(words):
  											word = words.split()
  											result = ""
  											for x in word:
  												result += x[0]
  												return result.upper()
print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

name = "Alpha"
number = len(name)*5
print("hello {} your lucky number is: {}".format(name, number))
base = 7.588
with_tva = 5.555
print("The base price is  ${:.1f} the price with tva is ${:.2f}".format(base, with_tva))
print("The base price is  ${:>3.3f} the price with tva is ${:.2f}".format(base, with_tva))
str = "Bamoye TRAORE"
print(str.replace("Bamoye", "Alpha"))
first = "Apple"
second = "pineapple"
third = "carrot"
print("{} {} {} are fruits to eat for sure".format(first, second, third))
print("{:b}".format(10))
print("{:.6s}".format("python"))
print("{:>.2s}".format("python"))
print("{:<6s}".format("py"))
print("{:^5s}".format("py"))
print("{:>10s}".format("py"))
top = "Tiger"
middle = "Hyena"
bottom = "Lion"
var1 = "pineapple"
var2 = "carrot"
var3 = "Apple"
print("Hello", var3)
print(f"Hey {var2} is cool")
print(f"Honestly {var3} is my favorite fruit")
print(f"Alpha TRAORE")
price = 5
amount = price*4
print(f"The price of one mango is {price}$ and {amount}$ for all")

"""
num = input("Enter the number >")
for x in range(len(num)):
  if num[x] != num[-1 -x]:
	print(f"{num} is not palindrome")
	break;
  print(f"{num} is palindrome")
  break

weather = "rainful"
print(weather[:4])

"""


def is_palindrome(input_string):
  # We'll create two strings, to compare them
  new_string = ""
  reverse_string = ""
  # Traverse through each letter of the input string
  for string in input_string.lower():
	# Add any non-blank letters to the 
	# end of one string, and to the front
	# of the other string. 
	if string.replace(" ",""):
		new_string = string + new_string
		reverse_string = string + reverse_string
  # Compare the strings
  if new_string[::-1]==reverse_string:
  	return True
  	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


def replace_ending(sentence, old, new):
  # Check if the old string is at the end of the sentence 
  if sentence.endswith(old):
	# Using i as the slicing index, combine the part
	# of the sentence up to the matched string at the 
	# end with the new string
	i = sentence.split()
	k = i[-1].replace(old, new)
	new_sentence = sentence[0:-len(old)]+k
	return new_sentence

  # Return the original sentence if there is no match 
  return sentence
  
  print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"



fruit = "pineapple"
print(fruit.count("p"))

weather = "rainful"
print(weather[:4])
leather = weather.replace("rainful", "bluelight")

print(leather)

def get_word(sentence, n):
  # Only proceed if n is positive 
  if n > 0:
  	words = sentence.split()
	# Only proceed if n is not more than the number of words 
	if n <= len(words):
		return(words[n-1])
		return("")

		print(get_word("This is a lesson about lists", 4))
		print(get_word("This is a lesson about lists", 5)) 
		print(get_word("Now we are cooking!", 1)) 
		print(get_word("Now we are cooking!", 4))

		fruits = ["pineapple", "Bananas", "Apple", "Mangoes", "Tomatoe"]
		print(fruits)
		print(len(fruits))
		fruits.insert(0, "orange")
		print(fruits)
		fruits.append("Melon")
		print(fruits)
		fruits.pop(2)
		print(fruits)

		def skip_elements(elements):
  # Initialize variables
  new_list = []
  i = 0

  # Iterate through the list
  for x in elements:
	# Does this element belong in the resulting list?
	if i <= len(elements):
	  # Add this element to the resulting list
	  new_list.append(elements[i])
	# Increment i
	i+=1
	

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


animal = ["Monkey", "Zebra", "Dolphin", "Rabbit", "Elephant"]
char = 0
for x in animal:
	char+=len(animal)
	print("Total characters: {}, Average lenght: {} ".format(char, char/len(animal)))

	winners = ["Papi", "Guindo", "Adiaratou"]
	for x, i in enumerate(winners):
		print("{}-{}".format(x+1, i))


		languages = ["Python", "Java", "Javascript"]
		prime_language = enumerate(languages)
		print(list(prime_language))
		for index, x in enumerate(languages, 100):
			print(index, x)

			def full_email(person):
				result = []
				for email, name in person:
					result.append("{} < {} >".format(name, email))
					return result
					print(full_email([("Bamoye TRAORE", "tbamoye96@gmail.com"),("Alex Potter", "alexample@gmail.com")]))

					multiple = []
					for i in range(1, 11):
						multiple.append(i*7)
						print(multiple)
						multiples = [x*8 for x in range(1,11)]
						print(multiples)
						add = [s*10 for s in range(1,11)]
						print(add)
						list = ["python", "java", "Javascript", "c", "ruby"]
						lenghts = [len(d) for d in list]
						print(lenghts)
						w = [z for z in range(101) if z % 5 == 0]
						print(w)
						print([x*11 for x in range(1,11)])

						filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [filenames[0], filenames[1].replace("stdio.hpp", "stdio.h"),
filenames[2].replace("sample.hpp","sample.h"), filenames[3], filenames[4].replace("math.hpp", "math.h"), filenames[5]]
print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


"""
def pig_latin(text):
  say = "ay"
  # Separate the text into words
  words = text.split()
  new_list = []
  for  word in words:
  lenght_of_word = len(word)
  
  first_letter = word[0]
  remove_first_letter = lenght_of_word[1:]
  pig_latin_word = remove_first_letter + first_letter + say
  # Create the pig latin word and add it to the list
  sentence = " ".join(words)
  # Turn the list back into a phrase
  return sentence
	
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) #

"""


def pig_latin(text):
	say = "ay"
  # Separate the text into words
  words = text.split()
  new_list = []
  for word in words:
  	for letter in word:

  		lenght_of_word = len(letter)
  		
  		first_letter = word[0]
  		remove_first_letter = lenght_of_word[1:]
  		pig_latin_word = remove_first_letter + first_letter + say
  # Create the pig latin word and add it to the list
  sentence = " ".join(words)
  # Turn the list back into a phrase
  return sentence
  
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) #