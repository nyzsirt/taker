from taker.config.config import *
# The queues to listen on.Defaults to default , which will listen on all queues.
QUEUES = ("bloomberg",)
# Max memory (in Mb) after which the process will be shut down. Use with PROCESS = [1-N] to
# have supervisord automatically respawn the worker when this happens.Defaults to 1
MAX_MEMORY = 128
# Max number of greenlets to use.Defaults to 1.
GREENLETS = 1
SCHEDULER_TASKS = [
    {"path": "tasks.bloomberg.Bloomberg", "params": {}, "interval": 1, "queue": "bloomberg"},
]
