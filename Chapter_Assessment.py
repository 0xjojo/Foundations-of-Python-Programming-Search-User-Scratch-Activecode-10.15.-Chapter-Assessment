#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
# Find the total number of characters in the file and save to the variable num.
file = open ('travel_plans.txt','r')
char = file.read()
num = 0 
for c in char :
    num = num + 1
#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
#Find the total number of words in the file and assign this value to the variable num_words.
f = open ('emotion_words.txt','r')
lines = f.readlines()
num_words = 0
for line in lines :
    words = line.split()
    for word in words :
        num_words = num_words + 1
#Assign to the variable num_lines the number of lines in the file school_prompt.txt.
file = open ('school_prompt.txt','r')
lines = file.readlines()
num_lines = 0
for line in lines :
    num_lines = num_lines + 1
#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
file = open ('school_prompt.txt','r')
all = file.read()
print(all)
beginning_chars = all[:30]
#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
file = open ('school_prompt.txt','r')
lines = file.readlines()
three = []
for line in lines :
    words = line.split()
    three.append(words[2])
#Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
file = open ('emotion_words.txt','r')
lines = file.readlines()
emotions = []
for line in lines :
    words = line.split()
    emotions.append(words[0])
#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
file = open ('travel_plans.txt','r')
text = file.read()
char = []
for c in text :
    char.append(c)
first = char[:33]
first_chars = ''.join(map(str,first))
print (first_chars)
#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
file = open ('school_prompt.txt','r')
lines = file.readlines()
char ='p'
p_words = []
for line in lines :
    words = line.split()
    for word in words :
        if char in word :
            p_words.append(word)
        else :
            continue