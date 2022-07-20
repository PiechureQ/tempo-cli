import argparse
import logging
from config import load_config 
from tempo import Tempo
from datetime import date

def log_time(tempo, task_id, date=str(date.today()), time=28800):
    tempo.post_worklog(task_id, date, time)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log time to Tempo 😎")
    parser.add_argument('task', metavar='task_id', type=str, help='Jira task id')
    args = parser.parse_args()
    print()

    CONFIG = load_config()

    tempo = Tempo(CONFIG.get('user', 'token'), CONFIG.get('user', 'account_id'), logging.DEBUG)

    log_time(tempo, args.task)
