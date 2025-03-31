import nltk
nltk.download('punkt_tab')  
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import TreebankWordTokenizer


corpus= "I am Ankit. I am a software engineer. I love coding. I am learning Python. I am also learning NLP. I am very excited about it."
print(corpus)

documents = sent_tokenize(corpus)
print(type(documents))

for sentence in documents:
    print(sentence)


# Tokenization
# paragraph into words
# sentence into words
print(word_tokenize(corpus))
print(type(word_tokenize(corpus)))

for word in word_tokenize(corpus):
    print(wordpunct_tokenize(word))

tokenizer= TreebankWordTokenizer()
print(tokenizer.tokenize(corpus))