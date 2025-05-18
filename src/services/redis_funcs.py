from redis import Redis
import time
import os

redis = Redis()

def redis_listener(channels: list):

    pubsub = redis.pubsub()

    pubsub.subscribe(channels) 

    while(True):

        message = pubsub.get_message(ignore_subscribe_messages=True)
        if message != None:
            print(message['data'].decode('utf-8'))

        time.sleep(0.5)

def set(key: str, value: str, ttl: int = None) -> bool:
    actual_ttl = ttl if ttl is not None else int(os.getenv("EXPIRE_TIME", "3600"))
    
    result = redis.set(key, value)
    
    if actual_ttl > 0:
        redis.expire(key, actual_ttl)
    
    return result
    
def get(key: str):
    data = redis.get(key)
    return data

def delete(key: str) -> bool:
    return bool(redis.delete(key))

def exists(key: str) -> bool:
    return bool(redis.exists(key))