from apscheduler.schedulers.background import BackgroundScheduler
from MainServer.database.EndedAuction import set_winner_for_ended_auctions

def schedule_task():
    scheduler = BackgroundScheduler()
    scheduler.add_job(set_winner_for_ended_auctions, 'interval', minutes=1)
    scheduler.start()
