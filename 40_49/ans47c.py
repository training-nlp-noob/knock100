#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

返事をする      と に は        及ばんさと 手紙に 主人は
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語（サ変接続名詞+を+動詞）
コーパス中で頻出する述語と助詞パターン
"""

from ans41c import f_41
essay = f_41()

# essay[5] が例文
#essay = essay[5:6]


forout = ""
for sentence in essay :
    for chunks in sentence :
        pos_list = [s.pos for s in chunks.morphs]
        if "動詞" in pos_list:
            zyutugo =[s.base for s in chunks.morphs if s.pos == "動詞"][0]
            #dicは 1述語にひとつ sortの順番をあわせるため
            dic = {}
            kaku = []
            kou = []
            target = 0
            for src in chunks.srcs:
                moto = sentence[src]
                if len([m.pos for m in moto.morphs if m.pos != "記号"]) >= 2:
                    if "助詞" == [m.pos for m in moto.morphs if m.pos != "記号"][-1]  \
                    and "を" in [m.base for m in moto.morphs if m.pos != "記号"][-1]  \
                    and "サ変接続" == [m.pos1 for m in moto.morphs if m.pos != "記号"][0] \
                    and "名詞" == [m.pos for m in moto.morphs if m.pos != "記号"][0] :
                        target = 1
                        zyutugo = "".join([m.surface for m in moto.morphs]) +zyutugo
                    elif "助詞" in [m.pos for m in moto.morphs]:
                        #key=項 value = 格
                        dic["".join([m.surface for m in moto.morphs])] = [m.base for m in moto.morphs if m.pos =="助詞"][-1]
                    else:
                        continue
            if target == 1:
                for k, v in sorted(dic.items(), key=lambda x:x[1]):
                    kaku.append(v)
                    kou.append(k)
                print(zyutugo, "\t", " ".join(kaku), "\t", " ".join(kou))
                forout += zyutugo + "\t" + " ".join(kaku) + "\t" + " ".join(kou) + "\n"


with open("ans47c_out.txt", "w") as w:
    w.write(forout)


"""
以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語（サ変接続名詞+を+動詞）
コーパス中で頻出する述語と助詞パターン


cat ans47c_out.txt | cut -f 1 |sort | uniq -c |sort -nr | head
cat ans47c_out.txt | cut -f -2 |sort | uniq -c |sort -nr | head

これでいいのかな
"""




"""
http://blog.livedoor.jp/yawamen/archives/51492355.html
lambda ってなんだ？？
"""
