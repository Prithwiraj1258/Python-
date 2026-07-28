#function is the first class object
def double_decker():
    print('standing the double decker')
    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun
# print(double_decker())
# print(double_decker()())
def do_something(work):
    print('work started')
    print(work)

    print('work ended')

#do_something (2)
do_something('ami busy')
def coding():
    print('coding in python')
