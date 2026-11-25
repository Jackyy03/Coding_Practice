class Solution:
    def reverseWords(self, s):
        
        raw_words = s.split(".")
        
        words =[]
        for w in raw_words:
            if w != "":
                words.append(w)
        
        words.reverse()
        return  ".".join(words)
        
        
        