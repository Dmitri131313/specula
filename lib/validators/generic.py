import traceback
import re

def iswebaddress(val, **kwargs):
    l = re.match(r"http.?://", val)
    if l == None:
        print('value must start with http:// or https://')
        return False
    return True

def isboolstring(val, **kwargs):
    errmsg = "not understanding value, needs to be 'true' or 'false'"
    try:
        if val.lower() != "true" and val.lower() != "false":
            print(errmsg)
            return False
        return True
    except Exception as msg:
        traceback.print_exc()
        print("not understanding value needs to be 'true' or 'false'")
        return False


def maxlen(val, **kwargs):
    try:
        length = kwargs['length']
        if len(val) > length:
            errmsg = "Item is too long max length is {}".format(length)
            print(errmsg)
            return False
        else:
            return True
    except Exception as msg:
        print("couldn't figure out item length")
        traceback.print_exc()
        return False

def ischoice(val, **kwargs):
    try:
        choices = kwargs["choices"]
        if val in choices:
            return True
        else:
            errmsg = "invalid choice, valid options are: {}".format(choices)
            print(errmsg)
            return False
    except:
        print("something went wrong")
        traceback.print_exc()
        return False

def isint(val, **kwargs):
    try:
        i = int(val)
        return True
    except ValueError as Msg:
        print("value is not an int")
        return False



