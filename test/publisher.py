import services.redis_funcs as redis_funcs
import time

channel_name1 = "login"
channel_name2 = "logout"

r = redis_funcs.Redis()

while True:
    r.publish(channel_name1, "MESSAGE 1")
    r.publish(channel_name2, "MESSAGE 2")
    time.sleep(2)