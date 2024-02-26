# PicoCTF Sleuthkit Intro

AUTHOR: LT 'SYREAL' JONES

Description
Download the disk image and use mmls on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
Download disk image
Access checker program: nc saturn.picoctf.net 64605


---

ダウンロードしたファイルの情報を**mmls**を使って調べて得られた情報を**nc**を用いてサーバーに渡す問題です。

ひとまずダウンロードすると.gzで圧縮されたファイルでした.

解凍します。

    gunzip disk.img.gz

得られたイメージファイルの情報を取得します。

    mmls disk.img

    DOS Partition Table
    Offset Sector: 0
    Units are in 512-byte sectors

        Slot      Start        End          Length       Description
    000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
    001:  -------   0000000000   0000002047   0000002048   Unallocated
    002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)

このLengthの部分が必要な情報になります。

この情報をncで回答を入力してフラグを入手します。



    nc saturn.picoctf.net 64605



picoCTF{mm15_f7w!}