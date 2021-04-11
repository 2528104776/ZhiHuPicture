#!/usr/bin/python
import requests,re,time,os
from concurrent import futures


params = {
  "include":"data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics",
  "offset":0,
  "limit":"5",
  "sort_by":"default",
  "platform":"desktop"}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
urls = [];result = [];fs = [];

def main(x):
    try:
        for i in range(10):
            url = f'https://www.zhihu.com/api/v4/questions/{x}/answers'
            res = requests.get(url, params = params,headers=headers)
            r = res.json()

            for i in re.findall(r'"https.*?(?<=")',str(r)):
                if 'jpg' in i:
                    img = i.replace('"', '')
                    result.append(img)
            params['offset'] += 5
    except:
        print("到底了！")

    rt = list(set(result))

    executor = futures.ThreadPoolExecutor(max_workers = 8)
    for url in rt:
        f = executor.submit(requests.get,url)
        fs.append(f)

    futures.wait(fs)

    for i in fs:
        if i.status_code==200:
            file = open(f'/storage/emulated/0/知乎图片/{int(time.time()*1000)}.jpg',mode = 'ab')
            file.write(res.content)
            print("写入成功！")
    file.close()
    print(f'总共获取美女图片{len(rt)}张.')


def topic():
    url = 'https://www.zhihu.com/api/v4/topics/19552207/feeds/top_activity'
    res = requests.get(url,headers = headers)
    for i in res.json()['data']:
        if i['target'].__contains__('question'):
            link = i['target']['question']['url']
            yield link

if __name__ == '__main__':
    os.system('mkdir /storage/emulated/0/知乎图片')
    info = re.search('\d+',input("请输入Answer页面的链接:")).group()
    main(info)
    # topic()

