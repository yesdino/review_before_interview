

def sort_lis(lis, sort_key, desc):
    # sort
    if len(sort_key):
        if sort_key != 'Location':
            lis = sorted(lis, key=lambda x: x[sort_key])
        else:
            lis = sorted(lis, key=lambda x: (x['Rack'],x['Bay'],x['Inline']))
        if desc:
            lis.reverse()
    else:
        sort_key = 'Location'   # default
        lis = sorted(lis, key=lambda x: (x['Rack'],x['Bay'],x['Inline']))
    return lis


def test_sort_lis():
    # 正常值


    # 异常值


    # 边界值

    pass


