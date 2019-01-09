#!/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = 'Benjamin'

import os
import datetime
import logging
from logging.handlers import RotatingFileHandler

# logger declaration
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Entries, Base


# query db to return list of entry beyond point in time
def get_old_entry_list():
    current_time = datetime.datetime.utcnow()
    onehour_ago = current_time - datetime.timedelta(hour=1)
    
    return session.query(Entries).filter_by(Entries.time_add > onehour_ago).all()

if __name__ == '__main__':
    # configure log file to rotate in 5 files of 5MB
    file_handler = RotatingFileHandler('/var/log/redfish/cron_activity.log', 'a', 5000000, 5)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # connect to local sqlite db
    engine = create_engine('sqlite:////tmp/redfish.db')
    if not os.path.isfile('/tmp/redfish.db'):
        Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # delete and log each deleted entry
    for entry in get_entry_list:
        session.delete(entry)
        session.commit()
        logger.info('deleting: {} at {}'.format(entry.name, entry.time_add))