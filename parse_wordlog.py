#!/usr/bin/env python
#_*_coding:utf-8_*_


"""
自动解析wordlog。
1. 标点符号的解析
2. 怎样确定是真正的上屏后退格
3. 怎样确定是输入中退格
"""


import json
import sys


def run():
    """
    入口
    """
    signal_up = u"-/:;()$&@\".,?!'[]{}#%^*+=_\|~<>€£¥•"

    for line in sys.stdin:
        line = line.strip()
        if line is None or len(line) < 2:
            continue
        _records = []
        try:
            obj = json.loads(line)
            # 基础属性
            records = obj['records']
            app = obj['app']
            mix = obj['mix']
            version = obj['version']
            ip = obj['ip']
            skin = obj['skin']
            numberRowEnable = obj['numberRowEnable']
            sys.stdout.write("\t\t".join([mix, version, ip, skin, str(numberRowEnable), app]))
            sys.stdout.write("\t\t")
            for i, sentence in enumerate(records):
                # 句子里面有很多句子
                _sentence = []
                for word in sentence:
                    # 词是基本的输入单位，需要记录的信息如下
                    _word = ""
                    _keys = []
                    # 如果是一次有效的上屏行为，word中最后一个json已定包含word 字段。
                    if u'word' in word[-1] and u'output' in word[-1]:
                        for js in word:
                            tmp_key = js[u'key']
                            # 普通按键 {"key":"e","x":"277","y":"115","time":"54471344"}
                            if u'x' in js and u'time' in js and len(js) == 4:
                                pass
                            # 输入中退格 {"key":"delete","cList":"[Y, You, Your]"}
                            if u'cList' in js and len(js) == 2:
                                pass
                            # 上屏后退格 {"key":"delete","delete":"1"}
                            if u'delete' in js and len(js) == 2:
                                tmp_key = u'up_' + tmp_key
                            _keys.append(tmp_key)

                            # 有效的上屏 {"key":"space","output":"goid ","input":"goid" 
                            # ,"index":"0","oriPos":"1","word":"goid","lang":"en","dictNames":"[100]",
                            # "engine":"simeji","app":"com.simeji.simejimonkeynote"} 
                            if u'word' in js and u'oriPos' in js:
                                _word = js[u'word']
                                if js[u'key'] in signal_up:
                                    _word = _word + js[u'key']

                    elif len(word) == 1:
                        js = word[0]
                        # 点击候选栏上屏 [{"key":"candidate","output":" for"}]
                        if u'key' in js and js[u'key'] == u'candidate' and u'output' in js:
                            _word = js[u'output']
                            _keys.append(js[u'key'])
                        # 只有一个标点符号  [{"key":".","x":"848","y":"614","time":"64484520","output":". "}
                        if len(js) == 5 and u'x' in js and u'output' in js:
                            _word = js[u'output']
                            _keys.append(js[u'key'])
                        # 表示searchtype的内容 [{"packageName":"com.facebook.orca","isSearchType":"true"}]
                        if u'packageName' in js and u'isSearchType' in js:
                            continue

                    else:
                        for js in word:
                            tmp_key = js[u'key']
                            # 上屏后退格 {"key":"delete","delete":"1"}
                            if u'delete' in js and len(js) == 2:
                                tmp_key = u'up_' + tmp_key
                            _keys.append(tmp_key)

                    _sentence.append((_keys, _word))
                _records.append(_sentence)
                        
        except Exception as e:
            print(e)
        print_record(_records)

def print_record(records):
    record = []
    for sentence in records:
        sen = []
        for word in sentence:
            _keys, _word = word
            #utf_input = ''.join([str(uni) for uni in _input])
            #utf_keys = ''.join([str(uni) for uni in _keys])
            utf_keys = ""
            if _keys and len(_keys) > 0:
                utf_keys = ' '.join([str(uni) for uni in _keys])
            utf_word = str(_word)
            sen.append(' '.join([utf_keys, utf_word]))
        record.append('\t'.join(sen))
    print('\t\t'.join(record))


if __name__ == '__main__':
    run()
