import requests
from bs4 import BeautifulSoup
import pprint
res=requests.get('https://news.ycombinator.com/news')
#print(res)
s=BeautifulSoup(res.text,'html.parser')
res1=requests.get('https://news.ycombinator.com/news?p=2')
s1=BeautifulSoup(res1.text,'html.parser')
#print(s.find_all('div'))
links1=s.select('.storylink')
subtext1=s.select('.subtext')
links2=s1.select('.storylink')
subtext2=s1.select('.subtext')
links1.extend(links2)
subtext1.extend(subtext2)

def create_custom_news(links,votes):
    hr=[]
    for idx,item in enumerate(links):
        vote=subtext1[idx].select('.score')
        if len(vote):
            points = vote[0].getText()
            if int(points.split(" ")[0])>=100:
                titile=links[idx].getText()
                href=links[idx].get('href',None)
                hr.append({'title':titile,'link':href,'Points':points})
    return sort_stories_by_score(hr)
def sort_stories_by_score(list1):
    return sorted(list1,key=lambda k:k['Points'],reverse=True)
        #return hr
pprint.pprint(create_custom_news(links1,subtext1))