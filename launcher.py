from subprocess import Popen
from time import sleep

PROCESS = []

while True:
    ANSWER = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, x - закрыть все окна: ')

    if ANSWER == 'q':
        break
    elif ANSWER == 's':
        PROCESS.append(Popen(['python', 'server/run.py'], 
                             start_new_session=True))

        for i in range(2):
            sleep(1.5)
            PROCESS.append(Popen(['python', 'client/run.py'], 
                                 start_new_session=True))
            
    elif ANSWER == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()
    