# -*- coding: utf-8 -*-

import itchat
import requests
import os
import random
import time

#获取相应的随机图片名
def get_image(project_name):
    image_path = 'C:/Users/w/Desktop/spider/scrapy_practice/' +project_name + '/full/'
    filename_list = []
    for p in os.listdir(image_path)[:32]:
        basename = p.split('/')[-1]
        filename_list.append(basename)
    image_basename = random.choice(filename_list)
    return image_path + image_basename

"""
#图灵机器人接口
def get_response(msg):
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '26681b3c80944f20a5e54a46b6844c50',
        'info': msg,
        'userid': 'wechat_robot',
        }
    r= requests.post(api_url, data=data).json()
    print r.get('text')
    return r.get('text')
"""
   
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    #return get_response(msg["Text"])
    #自己发给别人的也会被误认为是留言
    #if msg['User']['NickName'] != 'Chaos_':
    
    myUserName = itchat.search_friends()['UserName']
    #如果信息不是由自己发出的话
    if not msg['FromUserName'] == myUserName:
        if msg['Text'] == u'新垣结衣':
            itchat.send_image(get_image('yui_pic'), msg['FromUserName'])
        elif msg['Text'] == u'石原里美':
            itchat.send_image(get_image('tenyuan_pic'), msg['FromUserName'])
        elif msg['Text'] == u'长泽雅美':
            itchat.send_image(get_image('majiang_pic'), msg['FromUserName'])
        elif msg['Text'] == u'gakki':
            itchat.send_image(get_image('gakki_pic'), msg['FromUserName'])
        else:
            auto_reply = (u'[奸笑]本人暂时没空。欢迎回复“新垣结衣”或“石原里美”或“长泽雅美”获取美图。'
                            u'[机智]别回复“gakki”')
            itchat.send(auto_reply, msg['FromUserName'])
            leave_message = (u"[%s]收到好友%s的信息：%s" % 
                            (time.strftime('%Y-%m-%d %H:%M:%S',
                            time.localtime(msg['CreateTime'])),
                            msg['User']['NickName'], msg['Text']))
            itchat.send(leave_message, 'filehelper')
    
    
if __name__ == '__main__':
    #一定时间内重新登陆不用重新扫码
    itchat.auto_login(hotReload=True)
    itchat.run()   
