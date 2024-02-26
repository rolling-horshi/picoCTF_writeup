# PicoCTF rail-fence

---

AUTHOR: WILL HONG

Description
A type of transposition cipher is the rail fence cipher, which is described here. Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it?
Download the message here.
Put the decoded message in the picoCTF flag format, picoCTF{decoded_message}.

---

レールフェンス暗号と呼ばれるものを解く問題です。

>Wikipedia : [URL](https://en.wikipedia.org/wiki/Rail_fence_cipher)


初めて聞く暗号ですね。ただ仕組み自体は簡単そうです。


メッセージテキストを開くと以下のようになっていました。

    Ta _7N6D49hlg:W3D_H3C31N__A97ef sHR053F38N43D7B i33___N6

レール本数は４と書かれています。



[CyberCheff](https://gchq.github.io/CyberChef/)というサイトでレールフェンス暗号を解読できるようなので試します。


    The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997






