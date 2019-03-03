from taker.config.config import *
# The queues to listen on.Defaults to default , which will listen on all queues.
QUEUES = ("default", "bloomberg",)
# Max memory (in Mb) after which the process will be shut down. Use with PROCESS = [1-N] to
# have supervisord automatically respawn the worker when this happens.Defaults to 1
MAX_MEMORY = 2000
# Max number of greenlets to use.Defaults to 1.
GREENLETS = 4
# Run the scheduler.Defaults to False.
SCHEDULER = True
# Seconds between scheduler checks.Defaults to 60 seconds, only ints are acceptable.
SCHEDULER_INTERVAL = 0.5
# Seconds between worker reports to MongoDB.Defaults to 10 seconds, floats are acceptable too.
REPORT_INTERVAL = 0.5
SCHEDULER_TASKS = [
    {"path": "tasks.bloomberg.Bloomberg", "params": {}, "interval": 1, "queue": "bloomberg"},
]
