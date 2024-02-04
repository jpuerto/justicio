import time

import schedule

from src.etls.bopz.load import today


schedule.every().day.at("11:00").do(today)

while True:
    schedule.run_pending()
    time.sleep(1)
