class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText=text.replace(',', '').replace('?', '').replace('!', '').replace('.', '')
        # make text lowercase
        formattedText.lower()
        self.formattedText=formattedText
    def freqAll(self):        
        # split text into words
        words=self.formattedText.split('')
         
        # Create dictionary
        dict={}
        for i in set(words):
            dict[i]=words.count(i)

        return dict
           
    def freqOf(self,word):
        # get frequency map
        dict=self.freqAll()
        if word in dict:
            return dict[word]
        else:
            return 0
        
