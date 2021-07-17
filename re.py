import re
#find all instances of a certain letter
string="Hello I live on 14248 which and my phone number is 9099090942"
print(re.findall(r"\d",string))

#prints groups of numbers that are together
string="Hello I live on 14248 which and my phone number is 9099090942"
print(re.findall(r"\d+",string))

#searches for the word and it then prints it
if re.search("awesome","Isn't this an awesome view?"):
	print("You are awesome!")

#searches by the letter then splits the word on it
result = re.split(r's','Awesome')
print(result)

#searches for the word this in the sentence
words = "Isn't this an awesome view? but its the most awesome view ever"
searchWorld = re.findall(r"awesome", words)
print(searchWorld)
