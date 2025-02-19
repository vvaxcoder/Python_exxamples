def action2():
    print(1 + [])           # Возбуждает исключение TypeError

def action1():
    try:
        action2()
    except TypeError:       # Самая последняя соответствующая инструкция try
        print('inner try')

try:
    action1()
except TypeError:           # Этот обработчик будет выполнен, только если
    print('outer try')      # action1 повторно возбудит исключение