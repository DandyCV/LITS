import logging

logger = logging.getLogger('div')

def d(a, b):
    logging.debug('started function d')
    try:
        c = a / b
        logging.debug(f'd return {c}')
        return c
    except ArithmeticError as e:
        logger.exception('b is zero', exc_info=True)