_i = iter(EXPR)                 ➊
try:
    _y = next(_i)               ➋
except StopIteration as _e:
    _r = _e.value               ➌
else:
    while 1:                    ➍
    try:
        _s = yield _y           ➎
    except GeneratorExit as _e: ➏
        try:
            _m = _i.close
        except AttributeError:
            pass
        else:
            _m()
        raise _e
    except BaseException as _e: ➐
        _x = sys.exc_info()
        try:
            _m = _i.throw
        except AttributeError:
            raise _e
        else:                   ➑
            try:
                _y = _m(*_x)
            except StopIteration as _e:
                _r = _e.value
            break
    else:                       ➒
        try:                    ➓
            if _s is None:
                _y = next(_i)
            else:
                _y = _i.send(_s)
        except StopIteration as _e:
            _r = _e.value
            break
RESULT = _r