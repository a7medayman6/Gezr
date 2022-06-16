import Constants as const
import nltk
from nltk.corpus import stopwords
from pyarabic.araby import tokenize, is_arabicrange, strip_tashkeel
import pandas as pd
import json 

class ArabicStemmer:
    def __init__(self):
        nltk.download('stopwords')
        f = open('roots.json', 'r')
        self.roots = json.load(f)
        f.close()

    
    def stem(self, text, verbose=False):
        data = {}

        # tokenization and remove non-letters (tashkeel) and non-arabic words
        tokens = self.tokenize(text)

        # stop words removal
        tokens = self.removeStopWords(tokens)
        data['Tokens'] = tokens.copy()

        # normalization
        normalized_tokens = self.normalize(tokens)
        data['Normalized Tokens'] = normalized_tokens.copy()

        # remove definition articles
        def_removed_tokens = self.removeDefinitionArticles(normalized_tokens)
        data['Def Articles Removed'] = def_removed_tokens.copy()

        # remove suffixes
        sufx_removed_tokens = self.removeSuffixes(def_removed_tokens)
        data['Suffex Removed'] = sufx_removed_tokens.copy()

        # remove prefixes
        prfx_removed_tokens = self.removePrefixes(sufx_removed_tokens)
        data['Prefex Removed'] = prfx_removed_tokens.copy()

        # remove last suffix
        lst_sufx_removed_tokens = self.removeLastSuffix(prfx_removed_tokens)
        data['Last Suffex Removed'] = lst_sufx_removed_tokens.copy()

        data['Root'] = lst_sufx_removed_tokens.copy()

        text = ' '.join(lst_sufx_removed_tokens)

        if verbose:
            return text, pd.DataFrame(data)

        return text

    def tokenize(self, text):
        tokens = tokenize(text, conditions=is_arabicrange, morphs=strip_tashkeel)

        return tokens

    def removeStopWords(self, tokens):
        sw = stopwords.words('arabic')

        tokens = [token for token in tokens if not token in sw]

        return tokens

    def normalize(self, tokens):
        for i, token in enumerate(tokens):
            if token == 'الله': continue
            for k in const.Norm:
                for v in const.Norm[k]:

                    if v == 'ه':
                        if tokens[i].endswith(v):
                            tokens[i] = tokens[i][:-1] + k

                    elif v in tokens[i]:
                        tokens[i] = tokens[i].replace(v, k)
        return tokens

    def removeDefinitionArticles(self, tokens):
        for i, token in enumerate(tokens):
            if token == 'الله' or self.isRoot(token): continue
            for token_len in range(7, 3, -1):
                if len(tokens[i]) >= token_len:
                    for article in const.Articles[token_len - 3]:
                        if tokens[i].startswith(article):
                            tokens[i] = tokens[i][len(article):]

        return tokens

    def removeSuffixes(self, tokens):
        for i, token in enumerate(tokens):
            if token == 'الله' or self.isRoot(token): continue
            for token_len in range(8, 4, -1):
                if len(tokens[i]) >= token_len:
                    for suffix in const.Suffixes[token_len - 3]:
                        if tokens[i].endswith(suffix):
                            tokens[i] = tokens[i][: - len(suffix)]
                           
        return tokens
    
    def removePrefixes(self, tokens):
        for i, token in enumerate(tokens):
            if token == 'الله' or self.isRoot(token): continue
            for token_len in range(8, 3, -1):
                if len(tokens[i]) >= token_len:
                    for prefix in const.Prefixes[token_len - 3]:
                        if tokens[i].startswith(prefix):
                            tokens[i] = tokens[i][len(prefix):]
                            
        return tokens

    def removeLastSuffix(self, tokens):
        for i, token in enumerate(tokens):
            if token == 'الله' or self.isRoot(token): continue
            if len(token) >= 4:
                for suffix in const.Suffixes[1]:
                    if token.endswith(suffix):
                        tokens[i] = token[: - len(suffix)]
                        break    
                
        return tokens
    
    def isRoot(self, token):
        token_len = len(token)

        if token_len > 5 or token_len < 3:
            return False
        
        rootsList = self.roots[str(token_len)]

        if token in rootsList:
            return True
        
        return False
