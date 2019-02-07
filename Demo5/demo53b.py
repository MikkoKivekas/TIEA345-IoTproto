import redis
red = redis.StrictRedis(host='localhost', port=6379, db=0)
# avaimen asettaminen  
    #red.set('key','value')
# avaimen hakeminen  
    #red.get('key')
# publish  
    #red.publish("topic","value")
# subscribe  

while 1:
    pub = red.pubsub()
    pub.subscribe('satunnaisluku')
    viesti=pub.get_message() 
    if(viesti != None)
        print viesti["channel"]
        print viesti["data"]
        if viesti["data"] ==1:
            break
