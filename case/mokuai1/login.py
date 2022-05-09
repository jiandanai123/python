import unittest

import requests




class Login():

        def login(self,user, pwd):
            url = "http://192.168.3.111:17089/frame/api/SystemMoule/Account/login"
            body = {
                "username": user,
                "password": pwd
            }
            r = requests.post(url, json=body)
            result = r.json()
            return result['accessToken']


        def is_login_sucess(self,res):
            if "响应成功" in res:
                return True
            else:
                return False


    if __name__ == "__main__":
        login = Login()
        a = login.login("lyl","lyl123456")
        print(a)
        print(login.is_login_sucess(a))










