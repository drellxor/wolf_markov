import vk_api
from markov_wolf import MarkovWolf

if __name__ == '__main__':
    # session = vk_api.VkApi(token='c8767213cdfa52be374952b3eb9632c6d4ed4b442b8202ed295efba6520613f8d1eb109a2a302595a6b59')
    # api = session.get_api()
    #
    # uploader = vk_api.upload.VkUpload(api)
    # result = uploader.photo_wall([pic], group_id=201211851)

    wolf = MarkovWolf('dataset', 'pictures')
    quote, pic = wolf.make_quote()
    pass


    #api.wall.post(owner_id='-201211851', )