#Pico CTF Local Authority

>AUTHOR: LT 'SYREAL' JONES

>Description
>Can you get the flag?
>Go to this [website](http://saturn.picoctf.net:49386/) and see what you can discover.


ウェブサイトにアクセスします。

![image1](./images/saturn.picoctf.net_49386_.png)

適当なIDとパスでログインしてみます。


![image2](./images/saturn.picoctf.net_49386_login.php.png)


失敗しました。

ジャヴァスクリプトを見てみます。

'''

function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}

'''


パスワードとIDがべた書きされてます。ログインしてみます。


![image3](./images/saturn.picoctf.net_49386_admin.php.png)

フラグが出ました。

