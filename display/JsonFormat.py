
import json

dic = {'a': 1, 'b': 2, 'c': 3}
js = json.dumps(dic)
print(js)

dic = {'a': 1, 'b': 2, 'c': 3}
js = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ':'))
print(js)