def sockMerchant(n, ar):
    # sockList = ar.strip().split(' ')
    sockDic = {}

    for sock in ar:
        try:
            sockDic[sock] += 1
        except:
            sockDic[sock] = 1

    pairs = 0
    for style in sockDic:
        pairs += (sockDic[style] // 2)
    return pairs