class TextNormalization:
    def __init__(self,data):
        self.data=data
        self.start()
    def start(self):
        print('''
            1)Converting strings to lowercase
            2)Removing punctuation
            3)Removing Spl chars
            4)Handing Emoji's
            5)Removing Extra spaces
            6)Contractions(Expanding )
            7)Correcting the words
        ''')

    def strings_lowercase(self):
        #return updated text
        self.data = self.data.lower()
    
    def removing_punctuation(self):
        import string
        chars=self.data
        for char in string.punctuation:
            chars=chars.replace(char,'')
        self.data=chars
    def removing_spl_char(self):
        chars=self.data
        for char in chars:
            if not char.isalnum() and not ord(char)==32:
                chars=chars.replace(char,'')
        self.data=chars
    def handling_emoji(self):
        import emoji
        chars=emoji.replace_emoji(self.data,'')
        chars=emoji.demojize(self.data)
        self.data=chars
    def remove_extra_space(self):
        words=self.data.split()
        data=' '.join(words)
        self.data=data
    def contractions(self):
        import contractions
        self.data=contractions.fix(self.data)
    def correcting_words(self):
        from textblob import TextBlob
        corrected_words=TextBlob(self.data).correct()
        self.data=corrected_words
obj=TextNormalization("Hii$ ba#by😎")
print('1)Converting strings to lower case....')
obj.strings_lowercase()
print(obj.data)
print('2)Removing Punctuations......')
option=input('Enter Yes/No: ').lower()
if option=='yes':
    obj.removing_punctuation()
    print(obj.data)
else:
    print('U dont have any punctuations in ur data')
print('3)Removing Spl chars......')
obj.removing_spl_char()
print(obj.data)
print('4)Handing Emoji......')
option=input('enter Remove_emoji/Demoji: ').lower()
if option=='remove_emoji':
    obj.handling_emoji()
print('5)Removing Extra spaces......')
obj.removing_spl_char()
print(obj.data)
print('6)Contractions......')
obj.contractions()
print(obj.data)
print('7)Correcting the words......')
obj.correcting_words()
print(obj.data)
