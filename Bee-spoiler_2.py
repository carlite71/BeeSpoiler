import english_words

from english_words import english_words_lower_set as words


def bee_spoiler(word_list, central_letter, peripheral_letters):
  '''Solves the Spelling Bee of the New York times by creating a list of words that comply with the rules:'''
  '''Words must only include the provided letters. The central one is mandatory'''
  '''Words must be at least 4-letters long'''
  
  result = []
  
  letters = set(peripheral_letters) # create a set with the peripheral letters
  
  letters.add(central_letter) # add central letter to set. This is necessary to include more instances of the central letter.
  
  for word in word_list:
    
    word.lower() # convert to lowercase (or whatever case the word list is)
    
    word_letters = set(word) # creates a set with the letters
    
    if len(word) < 4 or central_letter not in word_letters: # words must be at least 4-letter long and include the central letter
      continue
    
    elif word_letters.issubset(letters):
      result.append(word)
      
  return sorted(result)
  
  
  

