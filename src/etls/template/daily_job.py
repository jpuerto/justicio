import time

import schedule

from src.etls.template.load import today


schedule.every().day.at("11:00").do(today, collection_name="<collection_name>")

while True:
    schedule.run_pending()
    time.sleep(1)