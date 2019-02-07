import redis
import random

red = redis.StrictRedis(host='localhost', port=6379, db=0)
# avaimen asettaminen  
    #red.set('key','value')
# avaimen hakeminen  
    #red.get('key')
# publish  
    #red.publish("topic","value")
    
while 1
  rand = random.randint(1,101)
  red.publish("satunniasluku",rand)
  sleep(1)
  if(rand ==1)
