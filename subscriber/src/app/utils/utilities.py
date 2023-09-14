

def str2dict(strval:str):
    s1 = strval.strip('{}')
    kv = s1.split(', ')
    return {k : v  for k,v in (kv_pair.split(': ') for kv_pair in kv)}