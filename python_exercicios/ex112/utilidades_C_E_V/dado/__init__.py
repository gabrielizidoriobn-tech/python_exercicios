def leiadinheiro(d):
    while True:
        msg = str(input(d))
        if ',' in msg:
            msg = msg.replace(',','.')
        if '.' in msg:
            break
        elif msg.isnumeric():
            break
        else:
            print(f'\033[31mresposta invalida, tente novamente!\033[m')
    return float(msg)
