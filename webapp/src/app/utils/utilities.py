from datetime import datetime as dt


iso8601_format = "%Y-%m-%dT%H:%M:%S.%f"

def str2dict(strval:str):
    s1 = strval.replace("'","").strip('{}')
    kv = s1.split(', ')
    ret_dict = dict()
    for k,v in (kv_pair.split(': ') for kv_pair in kv):
        if k == "timestamp":
            ret_dict[k]= dt.strptime(v,iso8601_format)
        elif k == "value":
            ret_dict[k]= float(v)
        elif k.startswith("_"):
            pass # Do Nothing for protected ids ( specific to MongoDB )
        else:
            ret_dict[k]=v
    return ret_dict
# EOF

