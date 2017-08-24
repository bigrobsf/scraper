import requests, csv
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/chart/toptv'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

shows = soup.select('td.titleColumn')

with open('top_shows.tsv', 'w') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    writer.writerow( ('Rank', 'Title', 'Stars', 'Debut') )

    rank = 0
    
    for show in shows:
        rank += 1
        title = show.select('a')[0].text
        stars = show.select('a')[0]['title']
        year = show.select('span.secondaryInfo')[0].text[1:5]
        writer.writerow( (rank, title, stars, year) )
