import requests, sys

headers = {
        'Cookie': 'cookie'
        }

data = {
        'StoreIp': '110.162.6.18',
        'StorePort': '6749',
        'cid': 8,
        'GroupId': 90,
        'StoreRpath': 'path'
        }

url='http://localhost:9090/store/register'

class Store:
    def __init__(self, ip, port, cid, gid, path):
        self.ip = ip
        self.port = port
        self.cid = cid
        self.gid = gid
        self.path = path

    def register(self):
        data = {
                'StoreIp': self.ip,
                'StorePort': self.port,
                'cid': self.cid,
                'GroupId': self.gid,
                'StoreRpath': self.path
                }

        resp = requests.post(url, data, headers=headers)
        print("request url: %s" % resp.request.url)
        print("return code: %d" % resp.status_code)

def main():
    store1 = Store('110.162.5.150', 6749, 8, 90, '/path')
    store2 = Store('110.162.5.225', 6749, 8, 90, '/path')
    stores = [store1, store2]
    for st in stores:
        st.register()

if __name__ == '__main__':
    sys.exit(main())


#print resp.status_code
#print resp.request.body
#print resp.text
#print resp.content



