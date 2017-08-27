
#
#  Test get_person
#
import vivotools as vt
import json
import string

grants = json.loads(open('grants.json').read())
k = len(grants["results"]["bindings"])
print k
words = {}
table = string.maketrans('=,:().+','       ')
for i in range(0,k):
    grant = grants["results"]["bindings"][i]
    title = grant["title"]["value"]
    for w in title.split():
        w = w.encode('ascii','ignore').translate(table).lstrip(' -').rstrip(' -')
        lw = w.lower()
        if len(lw) > 2 and lw != "the" and lw != "for" and lw != "a" and lw != "an" \
        and lw != "of" and lw != "and" and lw != "with" and lw != "" \
        and lw != "via" and lw != "it" and lw != "to" and lw != "in" \
        and lw != "on" and lw != "at" and lw != "during":
            words[w] = words.get(w,0) + 1
result = []
for w in sorted(words, key=words.get, reverse=True):
    result.append({"text":w,"size":words[w]})
    if len(result) >= 200:
        break
print json.dumps(result)
