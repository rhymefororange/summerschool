import bs4 as bs
import requests

sauce = requests.get('https://pythonprogramming.net/parsememcparseface/')
soup = bs.BeautifulSoup(sauce.content, 'lxml')
#sauce = requests.get('https://pythonprogramming.net/sitemap.xml')

# XML table extract
#soup = bs.BeautifulSoup(sauce.content, 'xml')
#for url in soup.find_all('loc'):
#    print(url.text)

# Page title with tags
#print(soup.title)

#Page title without tags
#print(soup.title.text)

# All text on the page
#print(soup.get_text())

# All links 1
#links = []
#for url in soup.find_all('a'):
#        print(url.get('href'))

# All links 2
#nav = soup.nav
#for url in nav.find_all('a'):
#    print(url.get('href'))

# Text of all paragraphs
#body = soup.body
#for para in body.find_all('p'):
#    print(para.text)

# Text of div with class 'body'
#for div in soup.find_all('div', class_='body'):
#    print(div.text)

# Javascript dynamic data test
js_test = soup.find('p', class_='jstest')
print(js_test.text)
