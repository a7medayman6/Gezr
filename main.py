import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from ArStem import ArabicStemmer

stemmer = ArabicStemmer()

text =  [
            "فاستضعفناهما",
            "المستصغرون",
            "فاسقيناكموها",
            "أفاستسقيناكموها",
            "وليتلطف"
            
        ]
str = "فاستضعفناهما المستصغرون فاسقيناكموها أفاستسقيناكموها وليتلطف"
stemmed, df = stemmer.stem(str)
print(df)

for sent in text:
#    stemmed, df = stemmer.stem(sent)
    pass




def tokenize(self, text):
    tokens = nltk.word_tokenize(text)

    return tokens

def removeStopWords(self, tokens):
    sw = stopwords.words('arabic')

    tokens = [token for token in tokens if not token in sw]

    return tokens