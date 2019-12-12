#!/usr/bin/env python
# coding: utf-8

# In[6]:


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
class Reversecipher: 
        
    def revencrypt(self,msg):
        self.msg=msg
        res=self.msg[::-1]
        return res
    
    def revdecrypt(self,msg):
        self.msg=msg
        res=self.msg[::-1]
        return res
    
class Doublecipher(Ceasercipher,Reversecipher):
    def dbencrypt(self,msg,key):
        self.msg=msg
        self.key=key
        encp_ceas=Ceasercipher().ceaserencrypt(msg,key)
        encp_rev=Reversecipher().revencrypt(encp_ceas,key)
        return encp_rev
    def dbdecrypt(self,msg,key):
        self.msg=msg
        self.key=key
        decp_rev=Reversecipher().revdecrypt(msg,key)
        decp_ceas=Ceasercipher().ceaserdecrypt(decp_rev,key)
        return decp_ceas


# In[ ]:




