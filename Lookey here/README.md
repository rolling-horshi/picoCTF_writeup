# PicoCTF Lookey here


***

>AUTHOR: LT 'SYREAL' JONES / MUBARAK MIKAIL

>Description
>Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.
>Download the data [here](https://artifacts.picoctf.net/c/126/anthem.flag.txt).



***



指定されたものを取得します。


'''

wget https://artifacts.picoctf.net/c/126/anthem.flag.txt

'''

テキストファイルなので開きます

'''
cat anthem.flag.txt
'''

文字がずらりと並んでいました。


'''

ANTHEM

      by Ayn Rand


        CONTENTS

         PART ONE

         PART TWO

         PART THREE

         PART FOUR

         PART FIVE

         PART SIX

         PART SEVEN

         PART EIGHT

         PART NINE

         PART TEN

         PART ELEVEN

         PART TWELVE




      PART ONE

      It is a sin to write this. It is a sin to think words no others
      think and to put them down upon a paper no others are to see. It
      is base and evil. It is as if we were speaking alone to no ears
      but our own. And we know well that there is no transgression
      blacker than to do or think alone. We have broken the laws. The
      laws say that men may not write unless the Council of Vocations
      bid them so. May we be forgiven!

'''


これらの文字列からフラグを取得します。

'''

cat anthem.flag.txt | grep pico

'''

picoCTF{gr3p_15_@w3s0m3_2116b979}

フラグが取得できました。




