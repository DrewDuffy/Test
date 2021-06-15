from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html_parser')


print(soup.prettify())
