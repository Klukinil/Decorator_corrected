import datetime

def file_path():
    path_inp= input('Введите путь к файлу(по умолчанию file_info_2.out): ')
    if path_inp == '':
        path_inp = 'file_info_2.out'
    return path_inp

def logger(PATH):
    def _logger(function_to_decorate):

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
            open(PATH, 'a', encoding="utf-8").write(f'{log}\n')
            new_function = function_to_decorate(*args, **kwargs)
            return new_function

        return wrapper
    return _logger

@logger(file_path())
def stand_alone_function(message):
   print(f'{message}')

stand_alone_function('выполнение кода!')

stand_alone_function('код выполняется!')