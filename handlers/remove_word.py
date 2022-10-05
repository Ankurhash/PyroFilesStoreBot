from configs.Config import REMOVE_WORD
async def rmw(cap):
    for i in REMOVE_WORD:
        try:
            cap1 = cap,replace(f"{i}","")
            cap = cap1
        except:
            pass
    return cap
