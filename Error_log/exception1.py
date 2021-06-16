import traceback
import logging
logging.basicConfig(filename='logger.txt',level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
#ogging.disable(logging.CRITICAL)#this is used to disable the logging
logging.debug('start of program')

try:
    n=9/0
    logging.debug("strart od exp")
    raise Exception("Check the expression")
except:
    file1=open('Error_log.txt',mode='a')
    file1.write(traceback.format_exc())
    file1.close()
    logging.debug("file closed")
    print("the traceback info was published in errorlog")