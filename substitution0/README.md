#PicoCTF substitution0

AUTHOR: WILL HONG

Description
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?
Download the message here.


---

暗号化されたメッセージを解読する問題です。

substitutionは置換という意味なので、置換が用いられる問題だと思われます。


メッセージの内容は以下です。

    ZGSOCXPQUYHMILERVTBWNAFJDK 

    Qctcnrel Mcptzlo ztebc, fuwq z ptzac zlo bwzwcmd zut, zlo gtenpqw ic wqc gccwmc
    xtei z pmzbb szbc ul fqusq uw fzb clsmebco. Uw fzb z gcznwuxnm bsztzgzcnb, zlo, zw
    wqzw wuic, nlhlefl we lzwntzmubwb—ex sentbc z ptczw rtukc ul z bsuclwuxus reulw
    ex aucf. Wqctc fctc wfe tenlo gmzsh brewb lczt elc cjwtciuwd ex wqc gzsh, zlo z
    melp elc lczt wqc ewqct. Wqc bszmcb fctc cjsccoulpmd qzto zlo pmebbd, fuwq zmm wqc
    zrrcztzlsc ex gntlubqco pemo. Wqc fcupqw ex wqc ulbcsw fzb actd tcizthzgmc, zlo,
    wzhulp zmm wqulpb ulwe selbuoctzwuel, U senmo qztomd gmzic Ynruwct xet qub eruluel
    tcbrcswulp uw.

    Wqc xmzp ub: ruseSWX{5NG5717N710L_3A0MN710L_357GX9XX}


ヒントを見ると頻度分析を用いると書かれていました。

https://en.wikipedia.org/wiki/Frequency_analysis


これを見ると、正直英語圏でない日本人では解きにくいように感じます。


なので、既存の文章から割り出すことにします。

最後の文章はおそらく

    The flag is:picoCTF

だと思われるので、ひとまずこれを用います。


置換していくと、最初の文章がアルファベットになっていることに気づきます。
なので、pythonで置換していきます。

```python

import string

txt_url = "substitution0/assets/message.txt"

txt = open(txt_url, 'r').read().lower()

alp = string.ascii_lowercase

t_dict ={}

for i in range(len(alp)):
    t_dict[txt[i]] = alp[i]

table = str.maketrans(t_dict)

txt = txt.translate(table)

print(txt)
```

結果がこちらです。

    abcdefghijklmnopqrstuvwxyz 

    hereupon legrand arose, with a grave and stately air, and brought me the beetle
    from a glass case in which it was enclosed. it was a beautiful scarabaeus, and, at
    that time, unknown to naturalists窶覇f course a great prize in a scientific point
    of view. there were two round black spots near one extremity of the back, and a
    long one near the other. the scales were exceedingly hard and glossy, with all the
    appearance of burnished gold. the weight of the insect was very remarkable, and,
    taking all things into consideration, i could hardly blame jupiter for his opinion
    respecting it.

    the flag is: picoctf{5ub5717u710n_3v0lu710n_357bf9ff}

フラグが取得できました。




