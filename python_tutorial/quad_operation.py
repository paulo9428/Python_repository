def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def multi(a,b):
    return a * b
def divid(a,b):
    if b == 0:
        return a
    return a / b

def input_calc():
    
    cmd = input("사칙연산 입력하시오(emxmple: 2 * 3)")

    cmds = cmd.split(' ')

    m = int (cmds[0])
    n = int (cmds[2])
    op = str (cmds[1]) 

    if op == '+' :
        r = add(m,n)
    elif op == '-' :
        r = sub(m,n)
    elif op == '*' :
        r = multi(m,n)
    elif op == '/' :
        r = divid(m,n)

    print("answer is {}".format(r))

    if cmds[0] == 'q' :
        x = input('종료하시겠습니까 [Y] OR [N]')
        if x == Y :
            break
        
            




