# Hidden Flag

## 手順
`chall.png`という画像ファイルが与えられるものの、pngのシグネチャに合致しないバイト列から始まっておりそもそも画像として読むことができない。そこでpngのシグネチャは最初の16バイトが一意に定まることを利用し、与えられた画像の先頭16バイトとの排他的論理和をとると10進数にして  
`105, 110, 118, 105, 115, 105, 98, 108, 101, 105, 110, 118, 105, 115, 105, 98`
であった。  
これは9バイトの鍵の繰り返しであると考えると、与えられたファイルを9バイトずつこの鍵で排他的論理和を取れば何らかのpngファイルが復元できると考えられる。  
したがってこの手順に従って与えられたファイルの復元を試みると無事にpngが復元されフラグが表示された。  
使用したコードは`hidden_flag.py`として添付した

## Flag
hsctf{n0t_1nv1s1bl3_an5m0r3?-39547632}
