import requests, csv
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/chart/toptv'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

shows = soup.select('tbody.lister-list tr')


def get_num_ratings(string):
    ratings = string.split(' ')
    num = ratings[3].split(',')
    if len(num) == 2:
        return num[0] + num[1]
    else:
        return num[0] + num[1] + num[2]


with open('top_shows2.tsv', 'w') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    writer.writerow(('Rank', 'Title', 'Stars', 'Debut', 'Rating', 'Num of Ratings'))

    rank = 0
    
    for show in shows:
        rank += 1
        title = show.select('td.titleColumn a')[0].text
        stars = show.select('td.titleColumn a')[0]['title']
        year = show.select('td.titleColumn span.secondaryInfo')[0].text[1:5]
        rating = show.select('td.ratingColumn strong')[0].text
        num_ratings = get_num_ratings(show.select('td.ratingColumn strong')[0]['title'])
        writer.writerow((rank, title, stars, year, rating, num_ratings))
