'''
create_time: 2024/1/23 17:33
author: yss
version: 1.0
'''

from prometheus_client import CollectorRegistry, Counter, push_to_gateway
registry = CollectorRegistry()
c = Counter('my_requests_total', 'HTTP requests total',  registry=registry)
c.inc()
push_to_gateway('10.130.13.32:8315', job='batchA', registry=registry)