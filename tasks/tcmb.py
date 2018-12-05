from mrq.task import Task
from mrq.context import log, connections, run_task
from mrq.basetasks.utils import JobAction


class ScheduledScans(Task):
    max_concurrency = 1

    def run(self, params):
        exchange = connections.mongodb_jobs.ex_usd_try

        mongo_counts = {
            '_id': 'mongo_counts',
        }
        exchange.update({"_id": "mongo_counts"}, mongo_counts, upsert=True)
