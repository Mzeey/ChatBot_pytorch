from tokenize import String
import nltk
#nltk.download("punkt") # This package contains a pretrained tokenizer; download on first run
from nltk.stem.porter import PorterStemmer

class LanguageHandler:
    Stemmer  = PorterStemmer()
    def tokenize(self, sentence):
        return nltk.word_tokenize(sentence)

    def stem(self, word = ""):#
        return self.Stemmer.stem(word.lower())
    
    def bag_of_words(self, tokenized_sentence, all_words):
        pass
