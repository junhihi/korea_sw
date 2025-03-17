def foo(name, /, **kwds):
    print(name)
    print(kwds)
    print(*kwds)
    
    return 'name' in kwds

print(foo(1, **{'name': 2}))
