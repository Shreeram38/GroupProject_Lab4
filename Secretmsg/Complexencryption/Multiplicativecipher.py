class Multiplicativecipher:
    def mulencrypt(self,msg,key):
            self.msg=msg
            self.key=key
            alphabet="abcdefghijklmnopqrstuvwxyz"
            newmsg=""
            flag=0
            if key%2==0 or key==1:
                print("key must be odd and greater than 1, within 26")
                return -1
            else:
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
                        newpos=(pos*self.key)%26
                        newchar=alphabet[newpos]
                        if flag==1:
                            newchar=newchar.upper()
                    else:
                        newchar=chr(ord(character)+self.key)
                    newmsg+=newchar
                return newmsg

    def muldecrypt(self,msg,key):
        self.msg=msg
        self.key=key
        alphabet="abcdefghijklmnopqrstuvwxyz"
        newmsg=""
        flag=0
        if key%2==0 or key==1:
            print("key must be odd and greater than 1, within 26")
            return -1
        else:
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
                    temp2=-1
                    for i in range(key,26):
                        if (key*i) % 26 == 1:
                            temp2=i
                    ans=temp2
                    newpos=(pos*ans)%26
                    newchar=alphabet[newpos]
                    if flag==1:
                        newchar=newchar.upper()
                else:
                    newchar=chr(ord(character)-self.key)
                newmsg+=newchar
            return newmsg
