import logging
import datetime
import os

file_path = os.path.join(os.path.dirname(__file__), 'logs', "ChatBot_{}.log".format(datetime.datetime.now().strftime('%d-%b-%Y')))
if not os.path.exists(file_path):
    with open(file_path, 'w+') as log_file:
        pass
logging.basicConfig(format='[%(asctime)s] p%(process)s - %(pathname)s:%(lineno)d - %(levelname)s - %(message)s',
                    handlers = [logging.FileHandler(file_path, 'r+', 'utf-8')])
log = logging.getLogger()
log.setLevel(logging.INFO)