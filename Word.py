class Word:

    def __init__(self,Word):
        self._word = Word

    def __str__(self):
        return self._word.lower()
    
    def __eq__(self,other):
     
        return sorted(self._word.lower()) == sorted(other._word.lower())
    
    
