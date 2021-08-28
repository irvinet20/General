import string
class LanguageHelper:
    def __init__(self, words):
        self._language = set()
        for i in words:
            self._language.add(i)

    def __contains__(self, query):
        word = query
        if word in self._language or word.lower() in self._language:
            return True
        else:
            return False
##    def EditLength(self, word):
##        d = 0
##        for r in range(0, len[word]):
##            if word
        
    def getSuggestions(self, query):
        sug = []
        alphabet_string = string.ascii_lowercase
        Lalphabet_list = list(alphabet_string)
        alphabet_string = string.ascii_uppercase
        Ualphabet_list = list(alphabet_string)
        ## 1 deletion check
        for r in range(0, len(query)):
            word = query[0:r]
            word = word + query[r+1:]
            if word in self._language or word.capitalize() in self._language:
                if word in sug:
                    pass
                else:
                    sug.append(word.lower())
            else:
                pass
        
        ##1 letter addition
        for r in range(0, len(query)):
            for i in range(0,26):
                word = query[0:r]
                word = word + Lalphabet_list[i]
                word = word + query[r:]
                if word.lower() in self._language:
                        if word in sug or word.capitalize() in sug or word.lower() in sug:
                            pass
                        else:
                            if query[0] == query[0].capitalize():
                                word = word.capitalize()
                                sug.append(word)
                            else:
                                sug.append(word.lower())
                if word.capitalize() in self._language:
                    if word in sug or word.capitalize() in sug or word.lower() in sug:
                        pass
                    else:
                            word = word.capitalize()
                            sug.append(word)
                else:
                    pass
        ## 1 letter change
        for r in range(0, len(query)):
            for i in range(0, 26):
                if query[r] == query[r].capitalize():
                    word = query[0:r]
                    word = word + Lalphabet_list[i]
                    word = word + query[r+1:]
                    if word.lower() in self._language:
                        if word in sug or word.capitalize() in sug or word.lower() in sug:
                            pass
                        else:
                            if query[0] == query[0].capitalize():
                                word = word.capitalize()
                                sug.append(word)
                            else:
                                sug.append(word.lower())
                    if word.capitalize() in self._language:
                        if word in sug or word.capitalize() in sug or word.lower() in sug:
                             pass
                        else:
                            word = word.capitalize()
                            sug.append(word)
                else:
                    word = query[0:r]
                    word = word + Lalphabet_list[i]
                    word = word + query[r+1:]
                    if word.lower() in self._language:
                        if word in sug or word.capitalize() in sug or word.lower() in sug:
                            pass
                        else:
                            if query[0] == query[0].capitalize():
                                word = word.capitalize()
                                sug.append(word)
                            else:
                                sug.append(word.lower())
                    if word.capitalize() in self._language:
                        if word in sug or word.capitalize() in sug or word.lower() in sug:
                             pass
                        else:
                            word = word.capitalize()
                            sug.append(word)
        ##invert
        for r in range(1, len(query)):
            word = query[0:r-1]
            word = word + query[r]
            word = word + query[r-1]
            word = word + query[r+1:]
            if word.lower() in self._language or word.capitalize() in self._language:
                if word in sug:
                    pass
                else:
                    if query[0] == query[0].capitalize():
                        word = word.capitalize()
                        sug.append(word)
                    else:
                        sug.append(word.lower())

        
        sug.sort()
        return(sug)
        

                
                
        
