def nitro_salt(m):
    try:
        m = int(m)
    except:
        m = 0
    return int(10 * m / 1000)
