import vk_api
import datetime
import time

while True:
    vk = vk_api.VkApi(token = 'd7842d0356f2b49288ba767dfc4deb50b82a8148894f410180dd0591d9568087cc750bcd6f3b1684b1927', scope = 'messages')
    delta = datetime.timedelta(hours = 6, minutes = 0)
    t = (datetime.datetime.now(datetime.timezone.utc) + delta)

    nowtime = t.strftime("%H:%M")
    nowdate = t.strftime("%d.%m.%Y")

    on = vk.method("friends.getOnline")  
    counted = len(on)
    vk.method('status.set', {'text': nowtime + ' * ' + nowdate + ' * ' + 'Друзей онлайн: ' + str(counted)})

    time.sleep(30)  