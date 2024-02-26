# PicoCTF Safe Opener

AUTHOR: MUBARAK MIKAIL

Description
Can you open this safe?
I forgot the key to my safe but this program is supposed to help me with retrieving the lost key. Can you help me unlock my safe?
Put the password you recover into the picoCTF flag format like:
picoCTF{password}

---

ファイルをダウンロードすると.javaファイルでした。

コードを見てみると、パスワードらしきものが書かれています。

    public static boolean openSafe(String password) {
            String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
            
            if (password.equals(encodedkey)) {
                System.out.println("Sesame open");
                return true;
            }
            else {
                System.out.println("Password is incorrect\n");
                return false;
            }
        }

これが怪しいですね。

"cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"

こちらを[CyberChef](https://gchq.github.io/CyberChef/)で復号できないか試してみます。

pl3as3_l3t_m3_1nt0_th3_saf3

できました。