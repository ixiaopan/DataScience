'''
down ebooks from BooksVooks, jinjiag
BooksVooks: https://booksvooks.com/
Jinjiang: https://www.jjwxc.net/
'''

import re
from bs4 import BeautifulSoup
import inquirer
import html2epub
from urllib.parse import urlparse
from urllib.parse import parse_qs
from tqdm import tqdm
import os
import requests


html_template = """
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
  </head>
  <body>
  {content}
  </body>
  </html>
"""

js_pattern = "<script.*<\/script>"
img_pattern = "(<img .*?src=\")(.*?)(\")"

def open_file(filepath):
  parent_directory = os.path.dirname(filepath)
  if not os.path.exists(parent_directory):
    os.makedirs(parent_directory)

  return open(filepath, 'w', encoding="utf8")


def get_html(url):
  r = requests.get(url)
  r.raise_for_status()
  r.encoding = r.apparent_encoding
  soup = BeautifulSoup(r.text, 'html.parser')
  return soup


def jinjiang(url):
  novel_id = parse_qs(urlparse(url).query)['novelid'][0]
  if not novel_id:
    return print('novel_id is empty!')

  f = open_file('jinjiang/' + novel_id + '.txt')
  chapter_list = get_html(url).find_all('a', attrs={'itemprop': 'url'})
  print('downloading chapters(' + str(len(chapter_list)) + ')...')
  for i, ch in enumerate(tqdm(chapter_list)):
    boj = get_html(ch['href'])
    content = boj.find('div', class_='noveltext')
    for div in content.find_all('div'):
      div.decompose()
    chapter = 'Chapter' + str(i+1) + '\n' + '\n'.join([para for para in content.stripped_strings]) + '\n'
    f.write(chapter)
  f.close()
  print('Success.')


def booksVbooks(url):
  domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
 
  def fix_img_src(m):
    if not m.group(2).startswith("http"): # relative path
      return ''.join([m.group(1), domain, re.sub('^\.\.', '', m.group(2)), m.group(3)])
    else: # abs path
      return ''.join([m.group(1), m.group(2), m.group(3)])

  query = parse_qs(urlparse(url).query)
  if 'page' in query: # must be in this format: ?page=1
    chapter_list = range(1, int(query['page'][0])+1)
  else: # read from the web page
    chapter_list = get_html(url).find(id='chapterlist').find_all('a')
  epub = html2epub.Epub(url.split('/')[-1].replace('.html', ''))
  print('downloading chapters(' + str(len(chapter_list)) + ')...')
  for i, ch in enumerate(tqdm(chapter_list)):
    if type(ch) == int:
      boj = get_html(re.sub(r'page=\d+', 'page='+str(ch), url))
    else:
      boj = get_html('https://booksvooks.com/' + ch['href'])

    chapter = str(boj.find('div', class_='bookfont force-overflow'))
    if chapter:
      chapter = re.sub(js_pattern, '', chapter) # remove inline scripts
      chapter = re.compile(img_pattern).sub(fix_img_src, chapter)
      chapter = html_template.format(content=chapter)

      chapter = html2epub.create_chapter_from_string(chapter, title='Chapter' + str(i+1))
      epub.add_chapter(chapter)
  
  # save
  epub.create_epub('booksVooks')
  print('Success.')


def main():
  questions = [
    inquirer.List(
      'source', 
      'Which source do you prefer?', 
      ['BooksVbooks', 'Jinjiang']
    )
  ]
  answers = inquirer.prompt(questions)

  url = input("Please input url: ")
  if answers['source'] == 'Jinjiang':
    # http://www.jjwxc.net/onebook.php?novelid=xxx
    jinjiang(url)
  else:
    # https://booksvooks.com/scrolablehtml/the-murder-of-roger-ackroyd-pdf-agatha-christie-1.html?page=130
    # https://booksvooks.com/selfish-shallow-and-self-absorbed-sixteen-writers-on-the-decision-not-to-have-kids-pdf.html
    booksVbooks(url)


if __name__ == '__main__':
  main()
