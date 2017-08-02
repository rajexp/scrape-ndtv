import requests
from bs4 import BeautifulSoup

def get_links(container):
    articles = list()
    for x in container:
        article = {}
        article.update({"image":x.find("img").get("src")})
        article.update({"link":x.find("a").get("href")})
        sibling = x.next_sibling
        if 'new_storylising_contentwrap' not in sibling.get("class",[]):
            continue
        article.update({"title":sibling.find("div",{"class":"nstory_header"}).a.get_text().strip()})
        article.update({"content":sibling.find("div",{"class":"nstory_intro"}).get_text()})
        articles.append(article)
    return articles

def linkRequest(res):
    soup = BeautifulSoup(res.text,'lxml')
    news_div = soup.findAll("div",{"class":"new_storylising_img"})
    return get_links(news_div)

def get_latest():
    index = 1
    articles = []
    while(True):
        url = 'http://www.ndtv.com/latest/page-'+str(index)
        res = requests.get(url)
        if res.status_code == 200:
            articles = articles + linkRequest(res)
            index += 1
        else:
            # No More Pages present
            break
    return articles
if  __name__ == "__main__":
    print(get_latest())
    

        
        
    
    