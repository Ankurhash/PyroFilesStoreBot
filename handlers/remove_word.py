from configs import Config
async def rmw(cap):
    for i in Config.REMOVE_WORD:
        if i in cap:
            try:
                cap1 = cap.replace(f"{i}","")
                cap = cap1
            except:
                pass
        else:
            continue
    return cap
