from ArStem import ArabicStemmer

stemmer = ArabicStemmer()


str = "فاستضعفناهما المستصغرون فاسقيناكموها أفاستسقيناكموها وليتلطف"
stemmed, df = stemmer.stem(str)
print(df)
print(stemmed)
