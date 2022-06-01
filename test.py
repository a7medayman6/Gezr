from ArStem import ArabicStemmer

stemmer = ArabicStemmer()

words = [ "استوصف", "اتبع", "تبعية", "المُستصغَرون", "فاستضعفناهُما", "أفاستسقيناكموها", "وليتلطف", "تجربة", "مخطئ", "أرشد", "الرَحمن", "مرحبا", "ركعة", "فاسقيناكموها", "ارتقب"]

stemmed, df = stemmer.stem(' '.join(words), verbose=True)

print(df)
