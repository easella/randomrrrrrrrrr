import pandas as pd
import os
os.system("pip3 install requests")
os.system("pip3 install bs4")
import requests
from bs4 import BeautifulSoup

url="https://www.cccmbca.org/sports/mbkb/2023-24/schedule?teamId=4dq8b4kwl3fnf1wo"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
months={"Nov":"11","Dec":"12",'Jan':"01","Feb":"02","Mar":"03","Oct":"10"}
shtml=requests.get("https://www.cccmbca.org/sports/mbkb/2012-13/schedule",headers=HEADERS).text
ssoup=BeautifulSoup(shtml)
teams=ssoup.find("select",{"class":"form-control form-select"})
games=[]
file=open('links.txt',"w")
file.write(str(""))
file.close()
file=open('options.txt',"w")
file.write(str(teams.find_all("option")))
file.close()
for option in teams.find_all("option"):
    link=option['value']
    link="https://www.cccmbca.org"+link
    file=open('links.txt',"a")
    file.write(str(link))
    file.write("\n")
    file.close()
    html=requests.get(link,headers=HEADERS).text
    ssoup=BeautifulSoup(html,features="html.parser")
    stable=ssoup.find("table")
    
    season=2012
    import time
    for i in range(1,2):
        time.sleep(2)
    
    
        soup=BeautifulSoup(html,features="html.parser")
    
        tables=soup.find_all("table")
        for table in tables:
        
            print('table')
        
            for tr in table.find_all("tr"):
                tds=tr.find_all("td")
    
                if  '<th>Date' not in str(tr) and 'Boxscore' in str(tr):
                    datez=tr.find_all("div",{"class":"nowrap d-block"})[0].text
                    datez=datez.replace("\r","")
                    datez=datez.replace("\t","")
                    datez=datez.replace("\n","")
                    datez=datez.replace("/xa0","")
                    datez=datez.strip()
                    schl=option.text
                    opp=tr.find_all("span")[1].text
                    venue=tr.find_all("span")[0]
                    
                    venue=venue.text
                
                
                    opp=opp.replace("\r","")
                    opp=opp.replace("\t","")
                    opp=opp.replace("\n","")
                    n=False
                    month=datez.split(".")[0]
                    month=month.replace("\r","")
                    month=month.replace("\t","")
                    month=month.replace("\n","")
                    month=month.strip()
                    result=tr.find_all("td")[2]
                    print(result)
                    if "W" in str(result):
                        result=str(result)
                        result=result.split("</span>,")[1]
                        result=result.replace("</td>","")
                        sp=result.split("-")[0]
                        op=result.split("-")[1]
                    else:
                        result=str(result)
                        result=result.split("</span>,")[1]
                        result=result.replace("</td>","")
                        sp=result.split("-")[1]
                        op=result.split("-")[0]
                    
                    year=season
                    sep="-"
                    if month=='Jan' or month=='Feb' or month=='Mar':
                        year=season+1
                    year=str(year)
                    month=str(month)
                
                    if len(month)>0:
                        month=month.replace(month,months[month])
                        date=year+sep+month+sep+datez.split(".")[1]
                    else:
                        date=date
                    if "neutral" in str(tr):
                        n=True
                    sp=sp.replace("\r","")
                    sp=sp.replace("\t","")
                    sp=sp.replace("\n","")
                    op=op.replace("\r","")
                    op=op.replace("\t","")
                    op=op.replace("\n","")
                    schl=schl.replace("\r","")
                    schl=schl.replace("\t","")
                    schl=schl.replace("\n","")
                    opp=opp.replace("\r","")
                    opp=opp.replace("\t","")
                    opp=opp.replace("\n","")
    
                

                    
                    games.append([date,schl,opp,venue,n,sp,op,2012])
print('done')
df=pd.DataFrame(games,columns=['Date','Schl','Opp','Venue','neutral','PTS','OPP','Year'])
df.to_csv("games.csv")
