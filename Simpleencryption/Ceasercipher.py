
class Ceasercipher:
    def __init__(self,key):
        self.key=key

    def ceaserencrypt(self,msg):
        self.msg=msg
        alphabet="abcdefghijklmnopqrstuvwxyz"
        newmsg=""
        flag=0
        for character in self.msg:
            if character >= 'A' and character <= 'Z':
                flag=1
            elif character >= 'a' and character <='z':
                flag=0
            else:
                flag=2
            if flag!=2:
                character=character.lower()
                pos=alphabet.find(character)
                newpos=(pos+self.key)%26
                newchar=alphabet[newpos]
                if flag==1:
                    newchar=newchar.upper()
            else:
                newchar=chr(ord(character)+self.key)
            newmsg+=newchar
        return newmsg
    def ceaserdecrypt(self,msg):
        self.msg=msg
        alphabet="abcdefghijklmnopqrstuvwxyz"
        newmsg=""
        flag=0
        for character in self.msg:
            if character >= 'A' and character <= 'Z':
                flag=1
            elif character >= 'a' and character <='z':
                flag=0
            else:
                flag=2
            if flag!=2:
                character=character.lower()
                pos=alphabet.find(character)
                newpos=(pos-self.key)%26
                newchar=alphabet[newpos]
                if flag==1:
                    newchar=newchar.upper()
            else:
                newchar=chr(ord(character)-self.key)
            newmsg+=newchar
        return newmsg

##Description
##Each letter of plain text is replaced by a letter with some fixed number of positions down with alphabet.
##Eg: A->D,B->E
