

class SearchFromList:

    def __init__(self,list_of_sen):
        self.dict_with_word = {

        }
        self.list_of_sen = list_of_sen

    
    def _create_dict_with_word(self):
        list_joined = " ".join(self.list_of_sen)
        words = list(set([word for word in list_joined.split(" ")]))
        for word in words:
            found_sentence = []
            for sentence in self.list_of_sen:
                if word in sentence.split(" "):
                    found_sentence.append(sentence)
            
            self.dict_with_word[word]= found_sentence
        
    def search_word(self,word):
        if len(self.dict_with_word) == 0:
            self._create_dict_with_word()
            return self.dict_with_word[word]
        else:
            return self.dict_with_word[word]


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
print(list_first.search_word("are"))