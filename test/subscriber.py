import services.redis_funcs as redis_funcs
import time

channel_name1 = "login"
channel_name2 = "logout"

r = redis_funcs.Redis()

p = r.pubsub()
p.subscribe(channel_name1, channel_name2)

while (True):
    r.publish(channel_name1, "MESSAGE 1")
    time.sleep(1)
    print(p.get_message())
    time.sleep(1)