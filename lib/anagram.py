# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        
    def match(self, word_list):
        #list to store matching anagrams
        matching_anagrams = []
        #converting word to lower case and sorting x-ter
        sorted_word = sorted(self.word.lower())
        #Iterating through each word in the list
        for candidate in word_list:
            #convert the candidate word to lowercase + sorting x-ter
            sorted_candidate = sorted(candidate.lower())
            
            #checking if words are equal and not identical
            if sorted_word == sorted_candidate and self.word.lower() != candidate.lower():
                matching_anagrams.append(candidate)
        
        return matching_anagrams
        