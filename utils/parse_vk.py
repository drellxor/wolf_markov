import vk_api
import time
import os

TIME_SLEEP = 0.4


def quotes_gen(api, domain, start_offset, count):
    offset = start_offset
    response = api.wall.get(domain=domain, count=count, offset=offset)
    while response['items']:
        print(offset)
        yield response['items']
        offset += count
        time.sleep(TIME_SLEEP)
        response = api.wall.get(domain=domain, count=count, offset=offset)


def parse(domain, offset):
    session = vk_api.VkApi(token='15a141c015a141c015a141c0f215c84df7115a115a141c049da9fbd33fe481faf2e4ace')
    api = session.get_api()

    file_folder = os.path.join(os.getcwd(), '../quotes')
    quotes_file = os.path.join(file_folder, f'{domain}.txt')
    pics_file = os.path.join(file_folder, f'{domain}_pics.txt')
    os.makedirs(file_folder, exist_ok=True)
    with open(quotes_file, 'a') as qf, open(pics_file, 'a') as pf:
        for quotes in quotes_gen(api, domain, offset, 100):
            for quote in quotes:
                if quote['marked_as_ads'] == 1:
                    continue
                qf.write(quote['text'] + '\n')
                for attachment in quote.get('attachments', []):
                    if attachment['type'] == 'photo':
                        pf.write(attachment['photo']['sizes'][-1]['url'] + '\n')


if __name__ == '__main__':
    parse('paccanskie_ponyatiya', 0)

