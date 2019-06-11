import logging

from RomanNumber import RomanNumber

fmt = '%(asctime)s :%(name)s :%(levelname)s - %(message)s'

logging.basicConfig(filename="roman.log", filemode='w', level=logging.DEBUG)
format = fmt

logging.debug('started class RomanNumber')
print(RomanNumber(631, 16))
logging.debug('done')

# logging.info('info')
# logging.debug('debug')
# logging.warning('warning')
# logging.error('error')