import requests,json
import pprint,os
from bs4 import BeautifulSoup
movie =("https://www.imdb.com/india/top-rated-indian-movies/")
page=requests.get(movie)
soup = BeautifulSoup(page.text,"html.parser")
Top_movie=[]
def scrap_top_list():
    print('running!!')
    main_div = soup.find("div",class_ ="lister")
    tbody = main_div.find("tbody",class_= "lister-list")
    trs=tbody.find_all("tr")
    movie_rank=[]
    movie_name=[]
    release_year=[] 

    for tr in trs:
        pos=tr.find("td", class_="titleColumn").get_text().strip()
        rank=""
        for i in pos:
            if "." not in i:
                rank=rank+i
            else:
                break
         
        movie_rank.append(rank)


        title=tr.find("td",class_="titleColumn").a.get_text()
        movie_name.append(title)

        year=tr.find("td",class_="titleColumn").span.get_text()
        release_year.append(year)

       
       
    
    details=()


    for i in range(0,len(movie_rank)):
        name =str(movie_name[i]).replace(' ',"").replace(':',"").lower()
        details = (int(movie_rank[i]),name,release_year[i])
       
        Top_movie.append(details) 
    os.environ = Top_movie
scrap_top_list()
