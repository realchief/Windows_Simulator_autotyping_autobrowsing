import webbrowser
from random import choice
import random
import newspaper
from newspaper import Article
from keyboard import *

news_urls = [
    'http://www.indiatimes.com',
    'http://www.bild.de/',
    'http://www.thesun.co.uk/',
    'https://www.nytimes.com/',
    'http://cnn.com',
    # 'http://sina.com.cn'
]

# news_lang = ['zh', 'en', 'de']


def scrapy_content_newsurl():
    article_urls = []
    news_url = choice(news_urls)
    # language = choice(news_lang)
    
    # if news_url == news_urls[5]:
    #     language = 'zh'
    print('news url: {}'.format(news_url))
    # print('language: {}'.format(language))
    
    news_paper = newspaper.build(news_url)

    try:
        for article in news_paper.articles:
            print('article url: {}'.format(article.url))
            article_urls.append(article.url)

        try_count = 0
        while True:
            if try_count > len(article_urls):
                scrapy_content_newsurl()

            else:
                url = article_urls[random.randint(0, len(article_urls)-1)]
                a = Article(url)
                a.download()
                a.parse()
                print('a: {}'.format(a))
                print('Authors: {}'.format(a.authors))

                text = (a.text).encode('utf-8')
                if text == "":
                    continue

                else:
                    print('Text: {}'.format(text))
                    keyboard.typewrite(text)
                    break
            try_count += 1

    except Exception as e:
        print('Exception: {}'.format(e))
        scrapy_content_newsurl()


if __name__ == '__main__':
    content = scrapy_content_newsurl()
    print ('content: {}'.format(content))