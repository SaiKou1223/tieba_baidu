import requests
import lxml.etree
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
}

def get_page(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        lxml = response.text
        lxml = re.sub("<!--","",lxml)
        lxml = re.sub("-->","",lxml)
# with open("tieba.html","w",encoding="utf-8") as f:
#     f.write(res)
        return lxml
    else:
        return None
'''
title = html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/text()')
print(title)
'''

def parse_html(html):
    html = lxml.etree.HTML(html)
    items = html.xpath('//li[@class=" j_thread_list clearfix"]')
    for item in items:
        try:
            title = item.xpath('./div//div[@class="threadlist_title pull_left j_th_tit "]/a/@title')[0]
            href = item.xpath('./div//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')[0]
            print("title:", title, "href:", "https://tieba.baidu.com" + href)
        except:
            pass

def main():
    url = "https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0"
    html = get_page(url)
    parse_html(html)

if __name__ == '__main__':
    main()