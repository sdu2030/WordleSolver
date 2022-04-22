# Function of program: To cheese the NYTimes daily Wordle puzzle
# https://www.nytimes.com/games/wordle/index.html
# Date: 4/14/2022


import json

with open("wordle_dictionary.json", "r") as f:
   wordles = json.load(f)


def specificLetterWords(letterList):
   
   letterList = list(letterList)
   valid = 0
   potentialWords = []
   
   
   # Checks how many 'valid characters' there are
   
   for x in letterList:
      if x.isalpha():
         valid += 1
   
   
   for words in wordles[0]["words"]:
      
      contains = 0
      
      # Checks if each letter of a word corresponds to the same spot as the specified input
      counter = 0
      while counter < len(letterList):
         if letterList[counter] == words[counter]:
            contains += 1
         
         counter += 1
      
      # If all letters match up it is added to a list of potential words
      if contains == valid:
         potentialWords.append(words)

   return potentialWords          
            
      
def unspecificLetterWords(letterList):
   letterList = list(letterList)
   potentialWords = []
   valid = 0
   
   for x in letterList:
      if x.isalpha():
         valid += 1
   
   for words in wordles[0]["words"]:
      
      tempWord = words
      contains = 0
      
      # Checks if specified letters are in the word

      for LLletters in letterList:
         if LLletters in tempWord:
            contains += 1
            
            # Removes checked letters to prevent the program from mislabeling a word as valid even if it doesn't contain enough duplicate letters
            tempWord = tempWord[0:tempWord.index(LLletters)] + tempWord[(tempWord.index(LLletters)+1):]
      
      if contains == valid:
         potentialWords.append(words)
   
   #
   for words in potentialWords:
      contains = 0
      
      # Checks if each letter of a word corresponds to the same spot as the specified input
      counter = 0
      while counter < len(letterList):
         if letterList[counter] == words[counter]:
            contains += 1
         
         counter += 1
      
      if contains > 0:
         potentialWords.remove(words)
   
   return potentialWords          

def invalidLetterChecker(potentialWords, letterList):
   letterList = list(letterList)
   
   counter = 0
   while counter < len(potentialWords):
      contains = 0
      
      counter1 = 0
      while counter1 < len(letterList):
         if letterList[counter1] in potentialWords[counter]:
            contains += 1
         counter1 += 1
      
      if contains > 0:
         potentialWords.remove(potentialWords[counter])
         counter -= 1
      
      counter += 1
   
   return potentialWords      
         
         

      

while True:
   # Accepting input:
   
   userGuess0 = input("Please enter yellow known letters, with spaces: ").lower()
   userGuess1 = input("Please enter green known letters, with spaces: ").lower()
   userGuess2 = input("Please enter invalid gray letters, in any order: ").lower()
   
   unspecific = unspecificLetterWords(userGuess0)
   specific = specificLetterWords(userGuess1)
   
   #print(unspecific)
   #print(specific)
   
   matches = list(set(specific).intersection(unspecific))
   matches = invalidLetterChecker(matches, userGuess2)
   
   print()
   print(str(len(matches)) + " satisfactory words found.")
   
   print(matches)
   
   exit = input("\n\nEnter [Q] to exit.\n").lower()
   if exit == "q":
      break
