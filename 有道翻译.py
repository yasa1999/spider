import time,random,hashlib
import requests

#ts: 13位的时间戳，字符串类型
#js 代码实现: ""+(new Date).getTime() //getTime()返回距 1970 年 1 月 1 日之间的毫秒数
#ts = str(int(time.time()*1000))
#print(ts)
#salt:
#js 代码实现:ts + parseInt(10 * Math.random(), 10);
#salt = ts + str(random.randint(0, 9))
#print(salt)
#sign
#js 代码实现:n.md5("fanyideskweb" + e + salt + "mmbP%A-r6U3Nw(n]BjuEU") //e通过断点调试 发现是为要翻译的单词
#n = hashlib.md5()
#b = ("fanyideskweb" + self.word + salt +
#"mmbP%A-r6U3Nw(n]BjuEU").encode(encoding="utf-8")
#n.update(b)
#sign = n.hexdigest()
#print(sign)

class youdao_spider(object):
    def __init__(self):
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        #self.word = input("请输入需要翻译的文本：")
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": "244",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": """OUTFOX_SEARCH_USER_ID_NCOO=2115110277.2255275; OUTFOX_SEARCH_USER_ID="1815334684@10.169.0.83"; _ga=GA1.2.1507711767.1572936072; _ntes_nnid=512ead0448a9e98df1aeefe4dd829235,1572939185170; JSESSIONID=aaaZCkVtZM90S6MDi8alx; JSESSIONID=abcnOjvjBUmUaghwyhblx; ___rl__test__cookies=1592381103258""",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

    def get_ts_salt_sign(self,word):
        ts = str(int(time.time()*1000))
        salt = ts + str(random.randint(0, 9))
        n = hashlib.md5()
        b = ("fanyideskweb" + word + salt +
             "mmbP%A-r6U3Nw(n]BjuEU").encode(encoding="utf-8")
        n.update(b)
        sign = n.hexdigest()
        return ts,salt,sign

    def translate_result(self,word):
        ts,salt,sign = self.get_ts_salt_sign(word)
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "c74c03c52496795b65595fdc27140f0f",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }
        res = requests.post(url=self.url,data=data,headers=self.headers)
        html =res.json()
        result = html['translateResult'][0][0]['tgt']
        print(result)

    def run(self):
        word = input('请输入要翻译的单词：')
        self.translate_result(word)


if __name__ == "__main__":
    spider = youdao_spider()
    spider.run()