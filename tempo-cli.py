import logging
import datetime
import time as time_module
import typer
from rich import print
from config import load_config
from tempo import Tempo
from datetime import date
from atlassian import Jira

CONFIG = load_config()

jira = Jira(
    url=CONFIG.get('user', 'jira_url'),
    username=CONFIG.get('user', 'jira_username'),
    password=CONFIG.get('user', 'jira_api_token'),
    cloud=True)

app = typer.Typer(help = "Log time to Tempo 😎")

@app.command('add', help="add worklog (today)")
def create_worklog(task_id: str = typer.Argument(..., help="jira task id"),
                   time: int = typer.Option(28800, help="time in seconds to add to worklog")):
    now = datetime.datetime.now(datetime.timezone.utc)
    formatted_date = now.strftime('%Y-%m-%dT%H:%M:%S.000+0000%z')
    print(f"add {time_module.strftime('%H:%M:%S', time_module.gmtime(time))} to {task_id}")
    res = jira.issue_worklog(task_id, started=formatted_date, time_sec=str(time))
    if res:
        print("👍")
    else:
        print("👎")

@app.command('rm', help="remove worklog (today)")
def delete_worklog(task_id: str = typer.Argument("", help="jira task id")):
    print(f"clear worklog for {task_id}")

@app.command('ls', help="list worklogs")
def list_worklogs():
    print("list worklogs")
    # res = jira.get_updated_worklogs(int(time_module.time()) - (24 * 60 * 60))
    # print(res)

@app.command('ls-tasks', help="list active task assign to user")
def list_tasks():
    print("Your active tasks:")
    query = 'project in (AR) AND status in ("W trakcie", "In Progress") AND assignee in (currentUser()) ORDER BY created DESC'
    res = jira.jql(query)
    issues = res['issues']
    if len(issues) > 0:
        for key in issues:
            print (key.get('key'))

if __name__ == "__main__":
    app()
