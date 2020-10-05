import datetime

def logger(function_to_decorate):

    def wrapper(*args, **kwargs):
        function_name = function_to_decorate.__name__
        current_date = datetime.date.today()
        current_time = datetime.datetime.now().time()
        print(current_date)
        log = {'current_date': str(current_date),
               'current_time': str(current_time),
               'function_name': function_name,
               'args': str(args)}
        log = str(log)
        print(log)
        open('file_info.out', 'a', encoding="utf-8").write(f'{log}\n')
        new_function= function_to_decorate(*args, **kwargs)
        return new_function

    return wrapper

if __name__ == '__main__':
    @logger
    def stand_alone_function(message):
       print(f'{message}')

    stand_alone_function('выполнение кода!')

    stand_alone_function('код выполняется!')




