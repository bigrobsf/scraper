import csv

def find_shows_by_year(year):
    with open('top_shows.tsv', 'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        rows = [row for row in list(reader) if year in row]
        return rows

# shows = find_shows_by_year('2002')
# for show in shows:
#     print('{}: {} - {}'.format(show[0], show[1], show[2]))


def find_shows_by_search_term(search_term):
    with open('top_shows.tsv', 'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        rows = [row for row in list(reader) if search_term.lower() in row[1].lower()]
        return rows

# titles = find_shows_by_search_term('Star')
# for title in titles:
#     print('{}: {} - {}'.format(title[0], title[1], title[2]))


def get_num_ratings(string):
    ratings = string.split(' ')
    num = ratings[3].split(',')
    return num[0] + num[1]


print(get_num_ratings("9.5 based on 266,235 user ratings"))