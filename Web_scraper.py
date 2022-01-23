import requests
from bs4 import BeautifulSoup
import pprint

pages = (1, 2)

for page in pages:
    res = requests.get(f"https://news.ycombinator.com/news?p={page}")
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')


    def stort_stories_by_votes(hnlist):
        return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


    def create_custom_hn(link, subtext):
        hn = []
        for idx, item in enumerate(link):
            title = item.getText()
            href = item.get('href', None)
            vote = subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ""))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
        return stort_stories_by_votes(hn)

    for next_page in soup.find_all('a'):
        print(soup.get_text('href="news?p=2"'))

    pprint.pprint(create_custom_hn(links, subtext))
