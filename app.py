# App To Search for sentences in list_of_sentences containing word

class SearchFromList:

    def __init__(self,list_of_sen):
        self._dict_with_word = {

        }
        self.list_of_sen = list_of_sen

    
    def _create_dict_with_word(self):
        list_joined = " ".join(self.list_of_sen)

        for word in list_joined.split(" "):
            found_sentence = []
            if not self._dict_with_word.get(word):
                for sentence in self.list_of_sen:
                    if word in sentence.split(" "):
                        found_sentence.append(sentence)
                
                self._dict_with_word[word]= found_sentence
        
    def _check_avaliability(self,word):
        if self._dict_with_word.get(word):
            return self._dict_with_word[word]
        else:
            return  "Not Found"
    
    def search_word(self,word):
        if len(self._dict_with_word) == 0:
            self._create_dict_with_word()
            return self._check_avaliability(word)
        else:
            return self._check_avaliability(word)
    
    
list_of_sentences = [
    "My name is Sagar",
    "I am Studying BSCCSIT",
    "I love Programming",
    "I am a python coder",
    "Who are you",
    "What is your name",
    "How are you",
]


list_first = SearchFromList(list_of_sentences)

print(list_first.search_word("is"))
print(list_first.search_word("am"))
print(list_first.search_word("How"))
print(list_first.search_word("I"))
print(list_first.search_word("ok"))
