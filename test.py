import requests

class xzs_login():
    def login(self,user,ps):
        url="http://192.168.55.45:8080/p2p_management/"
        header={
            "content-type": "application/json"
        }
        data = {
            "userName":user, "password":ps, "remember": False
        }
        r = requests.post(url=url, headers=header, json=data)
        return r.text

if __name__ == '__main__':
    x=xzs_login()
    x.login('tom','tom')
