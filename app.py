import vk_api
import datetime
import time

while True:
    vk = vk_api.VkApi(token = process.env.TOKEN, scope = 'messages')
    delta = datetime.timedelta(hours = 6, minutes = 0)
    t = (datetime.datetime.now(datetime.timezone.utc) + delta)

    nowtime = t.strftime("%H:%M")
    nowdate = t.strftime("%d.%m.%Y")

    on = vk.method("friends.getOnline")  
    counted = len(on)
    vk.method('status.set', {'text': nowtime + ' * ' + nowdate + ' * ' + 'Друзей онлайн: ' + str(counted)})

    time.sleep(30)  
