"""
url = 'https://wuhan.newhouse.fang.com/house/s/b9/'
需求：楼盘名，居室大小，区域，详细地址。房源特色，优惠活动，价格，电话
"""
import requests
from lxml import etree
def main():
    """
    通过分析，发现这个网站是静态的
    """
    url='https://wuhan.newhouse.fang.com/house/s/'
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
    }
    # 网页源代码
    r = requests.get(url,headers=headers).text
    # print(r)
    # 使用xpath进行数据提取
    ret = etree.HTML(r)
    # 拿到所有楼盘对应的标签
    li_list = ret.xpath('//div[@id="newhouse_loupan_list"]/ul/li')
    for li in li_list:
        # 楼盘名
        title = li.xpath('.//div[@class="nlcd_name"]/a/text()')[0].strip()
        # 居室大小
        size = li.xpath('.//div[contains(@class,"house_type")]//text()')
        size = ''.join(size) # 自动地将里面的内容敛平合并在一起
        size = size.replace('\n','').replace('\t','')
        # 区域
        area = li.xpath('.//span[@class="sngrey"]/text()')
        # area = li.xpath('.//span[@class="sngrey"]/text()')[0].strip()[1:-1]
        if area:
            area = area[0].strip()[1:-1]
        else:
            area = li.xpath('.//div[@class="address"]/a/text()')[0].strip()
            area = re.search('\[(.*?)\]',area).group(1)
        # 详细地址
        address = li.xpath('.//div[@class="address"]/a/@title')
        # 房源特色
        fangyuan = li.xpath('.//div[@class="fangyuan"]//text()')[0].strip()
        fangyuan = '-'.join(fangyuan)
        fangyuan = fangyuan.replace('\n','').replace('\t','')
        fangyuan = fangyuan[1:-1]
        # 优惠活动
        youhui = li.xpath('.//span[@class="color_s11"]/text()')
        if youhui:
            youhui = youhui[0]
        else:
            youhui = '暂无优惠'
        # print(youhui)
        # 价格
        price = li.xpath('.//div[@class="price_fix"]//text()')
        price = ''.join(price)
        price = price.replace('\n','').replace('\t','')
        if "总价" in price:
            price = price.split('(单价)')  # 以‘单价’来分割，以列表的形式返回
            price = price[0] +'(单价)'+'--' + price[-1]
        # 电话
        tel = li.xpath('.//div[@class="tel"]/p/text()')
        if tel:
            tel = ''.join(tel)
        else:
            tel = '暂无电话联系方式'
        print(title, size, area, address, fangyuan, youhui, price, tel)
if __name__ == '__main__':
    main()
