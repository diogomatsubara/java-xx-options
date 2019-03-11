# Very hacky script to convert the HTML table into a markdown formatted table.
from bs4 import BeautifulSoup


soup = BeautifulSoup(open('original.html').read())


for row in soup.find('tbody').findAll('tr'):
    if row.next.name == 'th':
        headers = [header.get_text() for header in row.findAll('th')]
        print("| {} | {} | {} | {} |".format(*headers))
        print("| --- | --- | --- | --- |".format(*headers))
    elif row.next.has_attr('colspan'):
        print("| {} | | | |".format(row.next.get_text().upper()))
    else:
        contents = [content.get_text().strip().replace('\n', ' ') for content in row.findAll('td')]
        print("| {} | {} | {} | {} |".format(*contents))


