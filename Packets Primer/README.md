# PicoCTF Packets Primer

---

Description
Download the packet capture file and use packet analysis software to find the flag.

Download [packet capture](https://artifacts.picoctf.net/c/196/network-dump.flag.pcap)


---


ダウンロードしたファイルは.pcmpファイルです。
これは**WireShark**というパケットキャプチャソフトで主に使うファイルです。

ファイルをWireSharkで開くと次の画面になります。

![image1](./assets/スクリーンショット%202024-02-26%20015452.png)


ここで上にある検索機能を使って、picoCTFのフラグでよくある**pico**で調べてみます。

が、検索結果に出ません。

調べる件数も少ないので一つ一つ調べてみることにします。

![image2](./assets/スクリーンショット%202024-02-26%20021517.png)

するとありました。
これがフラグでしょう。


---

では、なぜ検索で出なかったのでしょうか？

バイト列を見てみると以下のようになっていました。



    7020692063206f204320542046207b207020342063206b20332037205f2035206820342072206b205f20302031206220302061203020642036207d0a



これを[Cyber Cheff](https://gchq.github.io/CyberChef/)というサイトで調べてみます。

１６進数から文字列に変換し、そして余分なスペースを取り除きます。

![image3](./assets/スクリーンショット%202024-02-26%20022554.png)

フラグ：picoCTF{p4ck37_5h4rk_01b0a0d6}

検索に出なかった理由は文字列の間にスペース(0x20)が入っていたからでした。













