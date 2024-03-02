from pathlib import Path


LOG_DATA = Path(__file__).parent / 'log.txt'


class Log:
    def log (self, msg):
        raise NotImplementedError('Implemente o metodo log')
    
    def log_error (self, msg):
        return self.log(f'Error: {msg}')
    
    def log_sucess(self, msg):
        return self.log(f'Sucess: {msg}')
    

class LogFileMixin(Log):
    def log (self, msg):
        print(msg)
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_DATA, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    l = LogFileMixin()
    l.log_sucess('qualquer coisa')
    l.log_error('que legal')
    lp = LogPrintMixin()
    lp.log_sucess('qualquer coisa')
    lp.log_error('que legal')