# PicoCTF Search source

AUTHOR: MUBARAK MIKAIL

Description
The developer of this website mistakenly left an important artifact in the website source, can you find it?
The website is here

---

ページの中に隠されているものを探す問題です。

PicoCTFのこういう問題はフラグがべた書きされていることが多いので、ひとまずすべてのソースをあたります。


    .navbar-expand-md .navbar-nav .nav-link {
        padding: 15px 48px;
        font-size: 16px;
        color: #000;
        line-height: 18px;
    }
    /** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_8de925a7} **/
    .carousel-indicators li {
        width: 20px;
        height: 20px;
        border-radius: 11px;
        background-color: #070000;
    }
    .carousel-indicators li.active {
        background-color: #35a30a;
    }
    .carousel-indicators {
        left: inherit;
        top: 53%;
        width: 20px;
        display: block;
    }

.cssファイルの中に書かれていました。

**picoCTF{1nsp3ti0n_0f_w3bpag3s_8de925a7}**