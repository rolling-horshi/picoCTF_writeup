# PicoCTF patchme.py

---

AUTHOR: LT 'SYREAL' JONES

Description
Can you get the flag?
Run this Python program in the same directory as this encrypted flag.


---

ダウンロードしたファイルとフラグを同じフォルダに入れます。

ひとまずpythonファイルを見てみると、パスワードを入力すれば解読される仕組みだとわかります。


    ### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
    def str_xor(secret, key):
        #extend key to secret length
        new_key = key
        i = 0
        while len(new_key) < len(secret):
            new_key = new_key + key[i]
            i = (i + 1) % len(key)        
        return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
    ###############################################################################


    flag_enc = open('patchme.py/flag.txt.enc', 'rb').read()



    def level_1_pw_check():
        user_pw = input("Please enter correct password for flag: ")
        
        if( user_pw == "ak98" + \
                    "-=90" + \
                    "adfjhgj321" + \
                    "sleuth9000"):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), "utilitarian")
            print(decryption)
            return
        print("That password is incorrect")



level_1_pw_check()

---

user_pwがべた書きされているので、これを入力するか、コードに書いてフラグを入手します。


    user_pw = input("Please enter correct password for flag: ")
    user_pw = "ak98-=90adfjhgj321sleuth9000"
    if( user_pw == "ak98" + \
                "-=90" + \
                "adfjhgj321" + \
                "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return

フラグが入手できました。

picoCTF{p47ch1ng_l1f3_h4ck_f01eabfa}