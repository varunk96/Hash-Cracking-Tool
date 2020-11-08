import crypt

def testpass(CryptPass):
    salt = CryptPass[0:2]
    #print(salt)
    dictfile = open('varun.txt','r',encoding="ISO-8859-1")
    for word in dictfile.readlines():
        wordl = word.split("\n")
        w=wordl[0]
        #print(w)
        Cryptword = crypt.crypt(w,salt)
        #print("Cryptword : ", Cryptword)
        #print("ORiginal :", CryptPass)
        if Cryptword == CryptPass:
            print("Varun Sanjeev Kalia has found the Password :", w)
            exit()
        


def main():
    cryptpass = "23dNpxBzJg/Cg"
    testpass(cryptpass)

if __name__ == '__main__':
    main()