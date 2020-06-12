# coding:utf-8

import re
import pyperclip
import os


string = '''

举例来说，使用datetime.datetime.utcnow()、datetime.datetime.now()输出的类似2015-05-11 09:10:33.080451就是不带时区的时间（naive time），而使用django.util.timezone.now()输出的类似2015-05-11 09:05:19.936835+00:00的时间就是带时区的时间（Active time），其中+00:00表示的就是时区相对性。

'''

def cn_en_space(string):
    """ 中英文之间加空格 """
    # ()() 为一个元祖 有几个括号就有几个元祖元素
    # [] 为一个组 组内的条件关系为或
    pattern = re.compile(r'([A-Za-z0-9’!"#$%&\'()+,-./:;<=>?@`_]{0,})([\u4e00-\u9fa5\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b*]{0,})')
    finstrlist = pattern.findall(string)
    # print('str :'+str(finstrlist))
    lis = []
    for item in finstrlist:
        for tup_item in item:
            if tup_item:
                lis.append(tup_item)
    s = ' '.join(lis)
    s = s.strip()
    return s


ret_lis = []
string = string.strip("\n")     # 保留换行
arr = string.split("\n")
for string in arr:
    s = cn_en_space(string)
    ret_lis.append(s)
ret = '\n'.join(ret_lis)

print('\n转换后的字符串:\n')
print(ret)
pyperclip.copy(ret)             # 复制到剪切板


"""
字母: [A-Za-z]

中文: [\u4e00-\u9fa5]
中文符号: [\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]

过滤不了\\ \ 中文（）还有————
r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'      #用户也可以在此进行自定义过滤字符
 
者中规则也过滤不完全
r2 = "[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+"
 
\\\可以过滤掉反向单杠和双杠，/可以过滤掉正向单杠和双杠，第一个中括号里放的是英文符号，第二个中括号里放的是中文符号，第二个中括号前不能少|，否则过滤不完全
r3 =  "[.!//_,$&%^*()<>+\"'?@#-|:~{}]+|[——！\\\\，。=？、：“”‘’《》【】￥……（）]+"
 
去掉括号和括号内的所有内容
r4 =  "\\【.*?】+|\\《.*?》+|\\#.*?#+|[.!/_,$&%^*()<>+""'?@|:~{}#]+|[——！\\\，。=？、：“”‘’￥……（）《》【】]"

text = "\崔芸，\\我爱=+你！【我//""们】~————结/婚'吧:：！这.!！_#？?（）个‘’“”￥$主|意()不错......！"
print(re.sub(r1, , '', text))
"""
# -------------------------------------------------------------------------------------------------