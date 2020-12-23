import vk_api
from markov_wolf import MarkovWolf
import schedule
import time
import datetime
import const as c


def post_quote(wolf: MarkovWolf, session: vk_api.VkApi):
    quote, pic = wolf.make_quote()
    api = session.get_api()
    uploader = vk_api.upload.VkUpload(api)

    photo_data = uploader.photo_wall(pic, group_id=c.GROUP_ID)[0]
    api.wall.post(owner_id=-c.GROUP_ID,
                  from_group=1,
                  message=quote,
                  attachments=f'photo{photo_data["owner_id"]}_{photo_data["id"]}'
                  )
    print(f'{datetime.datetime.now()} - Done')
    pass


if __name__ == '__main__':
    wolf = MarkovWolf(c.DATASET_PATHS, c.DATASET_WEIGHTS, c.PICTURES_PATHS)
    session = vk_api.VkApi(token=c.ACCESS_TOKEN)

    schedule.every(c.POST_PERIOD).minutes.do(post_quote, wolf=wolf, session=session)
    while True:
        schedule.run_pending()
        time.sleep(1)
