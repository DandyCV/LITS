import logging

from div import d

#logging.basicConfig(level = logging.INFO)
fmt = '%(asctime)s :%(name)s :%(levelname)s - %(message)s'

logging.basicConfig(filename="sample.log", filemode='a', level=logging.DEBUG)
format = fmt

logging.debug('started function d')
print(d(1, 1))
logging.debug('done')

# logging.info('info')
# logging.debug('debug')
# logging.warning('warning')
# logging.error('error')


