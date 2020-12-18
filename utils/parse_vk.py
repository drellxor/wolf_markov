import vk_api
import time
import os
from utils.fix_chars import fix_text

TIME_SLEEP = 0.4


def quotes_gen(api, domain, start_offset, count):
    domain_name = domain
    owner_id = None
    if domain.startswith('public'):
        owner_id = -int(domain.replace('public', ''))
        domain = None

    offset = start_offset
    response = api.wall.get(owner_id=owner_id, domain=domain, count=count, offset=offset)
    while response['items']:
        print(f'{domain_name} : {offset}')
        yield response['items']
        offset += count
        time.sleep(TIME_SLEEP)
        response = api.wall.get(owner_id=owner_id, domain=domain, count=count, offset=offset)


def parse(domains, offset):
    session = vk_api.VkApi(token='68d51b3968d51b3968d51b398c68a097e1668d568d51b3937080ba8a113033b3eb9d18a')
    api = session.get_api()

    for domain in domains:
        file_folder = os.path.join(os.getcwd(), '../quotes')
        quotes_file = os.path.join(file_folder, f'{domain}.txt')
        pics_file = os.path.join(file_folder, f'{domain}_pics.txt')
        os.makedirs(file_folder, exist_ok=True)
        with open(quotes_file, 'a', encoding='utf8') as qf, open(pics_file, 'a', encoding='utf8') as pf:
            for quotes in quotes_gen(api, domain, offset, 100):
                for quote in quotes:
                    if quote['marked_as_ads'] == 1:
                        continue
                    qf.write(fix_text(quote['text']) + '\n')
                    for attachment in quote.get('attachments', []):
                        if attachment['type'] == 'photo':
                            pf.write(attachment['photo']['sizes'][-1]['url'] + '\n')


if __name__ == '__main__':
    parse([
        'public35661106',
        'public29714248',
        'sterva_sy4ka',
        'pizdaty_rebenok_i',
        'you_mudack',
        'gorday1',
        'public76892339'
    ], 0)

