from custom_kv_store import CustomKVStore

store = CustomKVStore('db.pkl')

# insert key-value pairs
store.put('key1', 'value1')
store.put('key2', 'value2')
store.put('key3', 'value3')

# get values by key
assert store.get('key1') == 'value1'
assert store.get('key2') == 'value2'
assert store.get('key3') == 'value3'

# delete key-value pairs
store.delete('key2')
store.delete('key3')

# get values by key
assert store.get('key1') == 'value1'
assert store.get('key2') == None
assert store.get('key3') == None

# delete pkl file
import os
os.remove('db.pkl')

