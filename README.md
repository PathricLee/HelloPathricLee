Feed Valuable Resource
===
feed资源价值体系打标签

快速开始
---
* 首先需要切换到工程的核心目录在feed_valuable_resource/predictor_sgm
* 下载环境依赖包：解压后，包含python和config两个目录：
  * 地址如下： scp liyabo01@cp01-lance.epc.baidu.com:/home/liyabo01/tools.tgz
  * 移动这两个目录python, config 到核心目录feed_valuable_resource/predictor_sgm下
* 执行示例：sh run.sh
  * 脚本里面首先配置python环境依赖的PATH和LD_LIBRARY_PATH
  * 执行python lib/predictor_sgm.py， 这个只是示例，如果要配置服务，需要在外面示例一个PredictorSgm对象,可以参考其main函数
* feed_valuable_resource/predictor_sgm下文件功能说明：
  * conf:  模型词典资源和模型关键配置
  * config: nlpc分词算子资源配置
  * lib： 模型主要代码，其中lib/predictor_sgm.py中类PredictorSgm的call函数是调用入口函数。外部进行实例化后调用call，输入json，输出返回码和json结果对象
  * python： 运行模型所需的python环境
  * run.sh： 运行模型例子，读取 sample_3.5k.json作为输入
  * sample_3.5k.json  3500条输入数据例子
  * src：非json格式输入，一般用于调试，可忽略
  * utilis： 词典解析等工具
  * log: 日志

输入输出示例
---
在传递给call函数的参数data，为一个gbk编码的json字符串，注意信息
* 模型请求，至少需要包含这4个字段，nid, title, url, vertical_type， 否则返回错误码和错误信息，对应说明详见下文
* vertical_type有一个过滤的环境，只有满足要求才会请求模型，被过滤掉的返回指定错误码和错误信息    

输入示例
INPUT | OUTPUT 
------------ | ------------- 
{"vertical_type": 0, "new_title_phrase_seg_list": ["最近", "财运", "好不好", "？", "看看", "面相", "就", "知道", "！"], "news_sub_category_v1": "综合", "new_title_basic_seg_list": ["最近", "财运", "好", "不", "好", "？", "看看", "面相", "就", "知道", "！"], "url": "http://baijiahao.baidu.com/s?id=1611187921927453327", "tj_tags": [["财运", 179], ["面相", 140], ["走路", 60], ["事业", 60], ["打扮一下", 57], ["化妆", 56], ["低着头", 52], ["面部", 52], ["昂首挺胸", 40], ["生意", 40], ["精神", 40], ["运势", 40], ["男性", 40], ["洗头", 40], ["面部表情", 40], ["穿着", 40], ["脚后跟", 40], ["头发", 40], ["机会", 37], ["表情", 35]], "general_tag": {"星座运势_运势分析": 876}, "title": "最近财运好不好？看看面相就知道！", "nid": "9136789095195298073", "news_sub_category": "综合", "news_sub_category_v2": "命理", "news_category_v2": "星座运势", "news_category_v1": "星座运势", "content": "看.....", "news_category": "女人", "tj_news_attention": [["财运", 674], ["星座运势", 597], ["命理", 434]]} | 0 {"url": "http://baijiahao.baidu.com/s?id=1611187921927453327", "nid": "9136789095195298073", "tags": [["实用价值:用", 39     5], ["知识攻略类", 395], ["知识分享", 395]]}
{"vertical_type": 14, "new_title_phrase_seg_list": ["小S", "难得", "娇羞", "依偎", "怀", "中", " ", "佘诗曼", "：", "惟有 ", "S", "妃", "深", "得", "我", "意", "！"], "new_sub_cate": "明星娱乐", "new_title_basic_seg_list": ["小S", "难得", "娇羞", "依偎", "怀", "中", " ", "佘诗曼", "：", "惟有", "S", "妃", "深", "得", "我", "意", "！"], "url": "https://baijiahao.baidu.com/s?id=1611187731878596983&wfr=content", "general_tag": {"娱乐_明星真人秀": 99}, "title": "小S难得娇羞依偎怀中 佘诗曼：惟有S妃深得我意！", "nid": "11638077156927223702", "video_type": "1", "new_cate": "娱乐", "manual_tags": ["小S", "佘诗曼     ", "明星"], "is_microvideo": 0} | 104 {"errno": 104, "err_msg": "infer request response null, not meet score_threshold", "nid": "11638077156927223702"} 


返回码含义说明
---
输入任何信息，都会有信息返回，返回码含义和说明如下
返回码 | 说明 | 返回示例
------------ | ------------- | -------------
0 | 正常，模型请求成功且阈值满足 | 0 {"url": "http://baijiahao.baidu.com/s?id=1611187877457271300", "nid": "9271092838454866351", "tags": [["实用价值:用", 93     0], ["知识攻略类", 930], ["知识分享", 930]]}
100 | requestdata json解析失败 | 100 {"errno": 100, "err_msg": "Parse json error, need check data"}
101 | requestdata 里面类型被过滤，不需要进入模型当前会用vertical_type 和 is_microvideo进行过滤 | 101 {"errno": 101, "err_msg": "type not need to do the model infer process", "nid": "7400822469713914958"}
102 | requestdata 里面缺失关键信息，例如，nid,title,url | 102 {"errno": 102, "err_msg": "some input attr is null, not allowed"}
103 | 模型返回值为空或者模型请求失败 | 103 {"errno": 101, "err_msg": "infer request response null", "nid": "714308224692231445558"}
104 | 模型返回的score 不满足阈值 | 104 {"errno": 104, "err_msg": "infer request response null, not meet score_threshold", "nid": "9229460792803913484"}
199 | 模型或者程序运行异常 | 199 {"errno": 199, "err_msg": "'NoneType' object has no attribute 'get'"}

如何贡献
---
贡献patch流程及质量要求

版本信息
---
本项目的各版本信息和变更历史可以在[这里][changelog]查看。


