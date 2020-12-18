import vk_api
from markov_wolf import MarkovWolf
import schedule
import time
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
    pass


if __name__ == '__main__':
    wolf = MarkovWolf(c.DATASET_PATH, c.PICTURES_PATH)
    session = vk_api.VkApi(token=c.ACCESS_TOKEN)

    schedule.every(15).minutes.do(post_quote, wolf=wolf, session=session)
    while True:
        schedule.run_pending()
        time.sleep(1)
