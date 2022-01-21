import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    # {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    #     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    # {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
    #     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    # ]



jobs = []
errors = []

def work(url):
        jobs = []
        errors = []
        domain = 'https://www.work.ua'
        url = 'https://www.work.ua/ru/jobs-kyiv-python/'
        resp = requests.get(url, headers=headers)
        if resp.status_code ==200:
                soup = BS(resp.content, 'html.parser')
                main_div = soup.find('div', id='pjax-job-list')
                if main_div:
                        div_lst = main_div.findAll('div', attrs={'class': 'job-link'})
                        for div in div_lst:
                                title = div.find('h2')
                                href = title.a['href']
                                content = div.p.text
                                company = 'Noname'
                                logo = div.find('img')
                                if logo:
                                        company = logo['alt']
                                jobs.append({'title': title.text, 'url': domain+href, 'description': content, 'company': company})
                else:
                        errors.append({'url': url, 'title': 'div does not exists'})
        else:
             errors.append({'url': url, 'title': 'page not response'})
        return jobs, errors

def rabota(url):
        jobs = []
        errors = []
        domain = 'https://rabota.ua'
        resp = requests.get(url, headers=headers)
        if resp.status_code ==200:
                soup = BS(resp.content, 'html.parser')
                main_div = soup.find('div', id='pjax-job-list')
                if main_div:
                        div_lst = main_div.findAll('div', attrs={'class': 'job-link'})
                        for div in div_lst:
                                title = div.find('h2')
                                href = title.a['href']
                                content = div.p.text
                                company = 'Noname'
                                logo = div.find('img')
                                if logo:
                                        company = logo['alt']
                                jobs.append({'title': title.text, 'url': domain+href, 'description': content, 'company': company})
                else:
                        errors.append({'url': url, 'title': 'div does not exists'})
        else:
             errors.append({'url': url, 'title': 'page not response'})
        return jobs, errors

if __name__ == '__main__':
        url = 'https://rabota.ua/zapros/pytnon/%D0%BA%D0%B8%D0%B5%D0%B2'
        jobs, errors = rabota(url)
        h = codecs.open('work.txt', 'w', 'utf-8')
        h.write(str(jobs))
        h.close()