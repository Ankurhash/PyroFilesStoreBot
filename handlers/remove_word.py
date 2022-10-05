from configs import Config
async def rmw(cap):
    for i in Config.REMOVE_WORD:
        try:
            cap1 = cap.replace(f"{i}","")
            cap = cap1
        except:
            pass
    return cap
