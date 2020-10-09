#!/usr/bin/env python
# -*- coding: utf-8 -*-
#中青看点提取read数据，使用thor的中青过滤器导出har文件，重命名为 1.har
import json
with open('1.har','r',encoding='utf8')as fp:
    json_data = json.load(fp)
    read_data = json_data['log']['entries']
    read_text = ""
    for i in range(len(read_data)):
        tmp = read_data[i]['request']['postData']['text']
        if i == len(read_data) - 1:
            read_text = read_text + tmp
        else:
            read_text = read_text + tmp + '&'
    #thor导出的文件会将消息中=解析成%3D,手动替换
    print(read_text.replace("%3D", "="))