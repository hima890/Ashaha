# function delete every record in database with more than 5days
from datetime import datetime
from models import Post
from projectFiles import db
from apscheduler.scheduler import Scheduler


cron = Scheduler(daemon=True)
# Explicitly kick off the background thread
cron.start()

@cron.interval_schedule(days=5)
def job_function():
    # Do your work here
    def delete():
    dateNow = datetime.now()
    records = Post.query.order_by(Post.date_created).all()
    for record in records:
        if (record.date_created.day - dateNow.day) >= 5:
            db.session.delete(record)
            db.session.commit()
        else:
            pass

# Shutdown your cron thread if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))




