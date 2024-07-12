def check_scope():
    def do_local():
        test='local test'
    def do_non_local():
        nonlocal test
        test='non local test'
    def do_global():
        global test #global variable
        test='global test'

    test='default'
    do_local()
    print('test value after do local:',test)
    do_non_local()
    print('test value after do non local:',test)
    do_global()
    print('test value after do global:',test)

#func do_local and other are local ,so they didnt call


check_scope()
print('test value after do non local:',test)