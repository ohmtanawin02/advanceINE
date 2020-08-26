from facebook_scraper import get_posts

for post in get_posts('thestandardth', pages=50):
    Ntext = post['text'][:100]
    if ('เรือดำน้ำ' in Ntext):
        print(Ntext)
        print('Likes: ', post['likes'])
        print('post: ', post['post_url'])
        print('link: ', post['link'])
        print('shares', post['shares'])
        print('------')