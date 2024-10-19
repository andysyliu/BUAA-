"""
url = "https://pvp.qq.com/web201605/herolist.shtml"
需求:将王者荣耀中所有英雄对应的所有皮肤爬取下来
"""
import requests
import os

def main():
    url="https://pvp.qq.com/web201605/js/herolist.json"
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
    }
    hero_list = requests.get(url,headers=headers).json()
    for hero in hero_list:
        # 英雄id
        ename = hero['ename']
        # 英雄名字
        cname = hero['cname']
        for i in range(1,2): # 实现所有英雄的十张图片地址
            # 那如果有些英雄没有10张壁纸呢？那就会出现404NOT found
            # 英雄图片地址
            hero_img_url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i}.jpg'
            print(hero_img_url)
            # 获取网址的响应对象
            response = requests.get(hero_img_url)
            # 如果相应对象使200，则可以保存图片，如果相应状态时404，则不可以保存图片
            if response.status_code == 200:
                print(hero_img_url)
                img_code = response.content
                with open(f'{word}/{cname}-{i}.jpg','wb') as f:
                    f.write(img_code)

if __name__ == '__main__':
    word ='王者荣耀皮肤'
    if not os.path.exists(word):
        os.mkdir(word)
    main()
