# -*- coding: utf-8 -*-
#来自初学者苦战三天的成果/苦笑
#学的内容有限，考核时间有限，用的代码都比较基础，所以编的有点长
def ks(L,P):      #设置默认参数好像要自定义函数
    if P=='':     #可能因为我的P是input引入的，然后默认参数老是出问题
        P=3       #我只能想到这样来解决
    for l in L:
        if l==' ':
            print(l,end='')     #感谢学长，感谢百度，它终于不换行了
        elif 96<ord(l)<123:     #大小写字母研究了好久/流汗
            if ord(l)+P>122:
                l=chr(ord(l)+P-26)    #感觉自己数学没学好/捂脸
                print(l,end='')
            else:
                l=chr(ord(l)+P)
                print(l,end='')
        elif 64<ord(l)<91:
            if ord(l)+P>90:
                l=chr(ord(l)+P-26)
                print(l,end='')
            else:
                l=chr(ord(l)+P)
                print(l,end='')
        else:
            l=chr(ord(l)+P)
            print(l,end='')
def disks(L,P=3):       #我看别人都搞了解密，从众一波
    if P=='':       #故技重施
        P=3
    for l in L:
        if l==' ':
            print(l,end='')
        elif 96<ord(l)<123:
            if ord(l)-P<97:
                l=chr(ord(l)-P+26)
                print(l,end='')
            else:
                l=chr(ord(l)-P)
                print(l,end='')
        elif 64<ord(l)<91:
            if ord(l)-P<65:
                l=chr(ord(l)-P+26)
                print(l,end='')
            else:
                l=chr(ord(l)-P)
                print(l,end='')
        else:
            l=chr(ord(l)-P)
            print(l,end='')
M=input('请选择模式:1.加密 2.解密')    #能力有限，超级低配版
M=int(M)
if M==1:
    L=input('请输入待加密内容:')
    P=input('请输入偏移量(默认3):')
    if P=='':        #默认不输入的值不可以int转换，卡了我好久
        pass         #说到底还是不会弄默认值/叹气
    else:
        P=int(P)
    ks(L,P)
elif M==2:
    L=input('请输入待解密内容:')
    P=input('请输入被偏移量(默认3):')
    if P=='':     #梅开二度
        pass
    else:
        P=int(P)
    disks(L,P)
else:        #本想再弄点啥的，后来发现啥不会弄/苦笑
    pass     #在无数次debug后，终于完成了，如果还有欠缺我也是尽力了，开肝git了，希望这份心血能交到你们手上（附加题无能为力了）