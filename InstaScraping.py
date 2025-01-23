from bs4 import BeautifulSoup
import requests
import instaloader

URL="https://www.instagram.com/{}/"

def parse_data(s):
    data={}

    s=s.split("-")[0]
    s=s.split(" ")

    data['followers']=s[0]
    data['following']=s[2]
    data['posts']=s[4]
    return data
def scrape_data(username):
    r=requests.get(URL.format(username))
    s=BeautifulSoup(r.text,"html.parser")
    meta=s.find("meta",property="og:description")
    return parse_data(meta.attrs['content'])

if _name=="main_":
    print(30*"=","Instagram",30*"=")
    username=input("enter userid=")
    data=scrape_data(username)
    print()
    print(username,"having",data["followers"],"followers")
    print(username,"having",data["following"],"following")
    print(username,"having",data["posts"],"posts")
    print(65*"=")
    photo=instaloader.Instaloader()
    photo.download_profile(username,profile_pic_only=True)