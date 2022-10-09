import logging 

def error(msg: str):
    logging.basicConfig(level=logging.ERROR, filename='logs_error.log')
    return logging.error(msg)
    
def info(msg: str):    
    logging.basicConfig(level=logging.INFO, filename='logs_info.log')
    return logging.info(msg)
