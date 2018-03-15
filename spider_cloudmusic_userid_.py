#encoding: utf-8

import requests
import random
import pymysql
import time

def random_useragent():
    #设置随机请求头
    useragentlists = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
                      'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
                      'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
                      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14',
                      'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
                      'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
                      'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0',
                      'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0']
    user_agent = random.choice(useragentlists)
    return user_agent

def save_userID_musql(userid,followed_s):
    #把信息存储到数据库中
    conn = pymysql.connect(host='localhost', user='root', password='123456', database='cloudmusic', port=3306,
                           charset='utf8')  # database为表名
    cursor = conn.cursor()
    sql = """
    insert into musiccloud_id(id,userid,follows) values(NULL ,%s,%s)
    """
    cursor.execute(sql,(userid,followed_s))  # 执行sql代码
    conn.commit()  # 需要提交才会真正运行sql
    conn.close()

def music_cloud_userID(user):
    #请求的请求头信息
    headers = {
        'User-Agent': random_useragent(),
        'Cookie': 'vjuids=1b7b12808.15adf36d6be.0.073499738b93; _ntes_nnid=45539279241bf1a6127332ceef82e2c5,1489803597547; _ntes_nuid=45539279241bf1a6127332ceef82e2c5; __gads=ID=323c9c084f15c3d4:T=1489803617:S=ALNI_MbErhpkw5vXUfbOEiRyfv-8aqz3iw; usertrack=c+5+hljTqmDCwEtFA/h/Ag==; mail_psc_fingerprint=4803dd05e9f9bb8181f188a8d1476146; Qs_lvt_73318=1505006022; Qs_pv_73318=2916726222229302000; UM_distinctid=15e8d8bb2630-029d8868aa4602-4e47052e-100200-15e8d8bb264199; NTES_CMT_USER_INFO=75602722%7C745447374%7C%7Cfalse%7CNzQ1NDQ3Mzc0QHFxLmNvbQ%3D%3D; __oc_uuid=b3f04ce0-1a08-11e7-8eba-c5c9514f5488; _ga=GA1.2.34698276.1490442809; _qddaz=QD.ej0isl.j92zxl.jaaspiy9; __e_=1513696157266; _iuqxldmzr_=32; NTES_YD_PASSPORT=s9sfCxAuBgzRNkuowEbshtHbTnyIaZ.P36qeOxz0Opval.DwlvG8Q0iRbElHYf.wsbnnAl9V.lVi71M6l3zUj.WtVNrELVPOCLm5or8upGsBYu53tE.kHlwNTKXktOIKK; KAOLA_ACC=yd.342635dd5bee4862a@163.com; __f_=1517292443515; __utma=187553192.34698276.1490442809.1517467077.1517473618.7; __utmz=187553192.1517473618.7.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; vinfo_n_f_l_n3=1f315448c25a9e5a.1.310.1489803610520.1517966727979.1519357553269; __remember_me=true; Province=020; City=020; vjlast=1489803597.1520579792.11; __utmc=94650624; MUSIC_U=a2ce8e7fd443aed07dc39143235e999f4a426cd3f77e9ddc25879395d418af5e52f6f24b5942ef64f6ab656c11185291a70b41177f9edcea; __csrf=dc1e0c2e996e20372e419f1448e2d1f1; __utma=94650624.34698276.1490442809.1520912057.1520917080.39; __utmz=94650624.1520917080.39.17.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=27qlTTq4u9kUhpFZg%5CZu2lxC3Q4cR38ZoRbAyRmBa%5C%5CEebQrn7qyIP7hclkg0DDKNS9MYJx4RA4%2FMQ17GBAAbwCBSKY0crl%2BF95OQcTq4pI4%2FyAmNROdT6nIJFoUJ18N12Dn4Za%2FRfaUtovAtip0gxUN27xr5N0jKheANRjcNr3GM%5CQA%3A1520920817302',
        'Referer': 'http://music.163.com/user/follows?id=74029445',
        'Origin': 'http://music.163.com',
        'Host': "music.163.com",
        'Pragma':'no-cache',
        'Proxy-Connection':"keep-alive"
    }
    #需请求的url（自己61056276）
    url = 'http://music.163.com/weapi/user/getfollows/%d?csrf_token=dc1e0c2e996e20372e419f1448e2d1f1'%(user)
    #Post的参数请求
    data = {
        'params': "bCIU6D3nKNcJQHyjMN+hHj5LAI54Cyis0eOFV3L8mO0msELnA5fk62PqOh5orb2yCtPUMgZz59EYSkC7A01wW7gvEc7i9LjRHhGD53fJi7sf/WMCSeJTKBjRcqUapY6H5Ss19zpv8V9wrl07kkJKpOklH6c7NBnYTnvrlqMl8MxHQDO/ECA/jBXFz0fLMGXDh82rwzXTvWHaEdE7zgJx5g==",
        'encSecKey': "7e50b9fac2b333634a481fe9c05d44d2d43eb46d3e2f2e7cfd03821c3dbbf1ae3f210039691d81ddb1182726aa7ea828338c3eaed3726fe4a522db52e1f741d42038a223f1dab3be72e8e60f8af4b37cb9c251945a8cb00e07b105c35327c425ba83c379832a866a5fbbac63a56cc878471ae20a9e6693f5ed9e225c6b205a36"
    }
    #获取返回的信息
    response = requests.post(url, headers=headers, data=data)
    try:
        follows = response.json()["follow"]
        print(follows)
    except KeyError:
        print("*"*70)
        print("找不到网站内容")
        print("*"*70)
        time.sleep(120)
        follows = []
    finally:
        follows_list = []
        if follows :
            for follow in follows:
                userid = follow["userId"]
                followed_s = follow["follows"]

                # 保存到列表中
                follows_list.append([userid,followed_s])

                # 把数据保存的数据库中
                save_userID_musql(userid,followed_s)
            print(follows_list)
            return follows_list
        else :
            return []


if __name__ == '__main__':
    temp_list = music_cloud_userID(user=633870037)
    #已爬取的列表
    saved_list = [633870037]
    #待爬取的列表
    wait_list = []

    while True:
        for i in range(len(temp_list)):
            #如果该用户没被爬取过且关注数大于0
            if temp_list[i][1] > 0 and temp_list[i][0] not in saved_list:
                #保存到待爬取列表中
                user = temp_list[i][0]
                wait_list.append(user)

        #从待爬列表中获取用户进行递归
        for i in range(len(wait_list)):
            #如果该用户没有爬过
            if wait_list[i] not in saved_list:
                user_spidering = wait_list[i]
                wait_list.pop(i)
                saved_list.append(user_spidering)
                temp_list = music_cloud_userID(user_spidering)
                # time.sleep(5)
                break

