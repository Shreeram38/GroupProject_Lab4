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


##Description:
##Inherits features of both Ceasercipher and Doublecipher .
##Eg:- HELLO -> OLLEH -> PMMFI