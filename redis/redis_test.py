from redis_util import Redis_update

# testing git hub

obj = Redis_update()
obj.set_key("jagdeep", "Yadav")
obj.add_hash_key('caste', 'jagdeep', 'yadav')
print(obj.get_hash_key('caste', 'jagdeep'))
print(obj.get_key('jagdeep'))
print(obj.get_all('caste'))