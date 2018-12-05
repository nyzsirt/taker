from config import *

# The queues to listen on.Defaults to default , which will listen on all queues.
QUEUES = ("default", "isbank")
# Max memory (in Mb) after which the process will be shut down. Use with PROCESS = [1-N] to
# have supervisord automatically respawn the worker when this happens.Defaults to 1
MAX_MEMORY = 2000
# Max number of greenlets to use.Defaults to 1.
GREENLETS = 5
