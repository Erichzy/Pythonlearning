from urllib import request

if __name__ == "__main__":
    url = "http://www.baidu.com"

    rsp = request.urlopen(url)

    html = rsp.read()

    html = html.decode()

    print(html)