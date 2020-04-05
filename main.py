from _datetime import datetime

def logger(func):
    def write_log():
        logfile_name = 'log.txt'
        with open(logfile_name, 'a', encoding='utf-8') as file:
            file.write(f'Function "some_function" was called at: {str(datetime.now())}\n')
        func()
    return write_log


@logger
def some_function():
    print('Function is doing something...')

some_function()