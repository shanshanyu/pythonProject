'''
create_time: 2024/1/24 12:36
author: yss
version: 1.0
desc: sdg_ingestion_job_failed_times_total  指标名称，每个任务作为一个 label 的值
上个版本不能及时更新数据表,在循环中加了一行，每次循环更新 任务表
'''

import time
import pymysql
from prometheus_client import CollectorRegistry, Counter, push_to_gateway
from hyperion_client.hyperion_inner_client.inner_config_manager import InnerConfigManager


class MonitorSDGJob:
    pushgateway_address = 'meta01.classic-ali-beijing-01.qimaoxiaoshuo.deploy.sensorsdata.cloud:8315'
    #pushgateway_address = '10.130.13.32:8315'
    # pushgateway_address = '10.20.20.218:8315'

    def __init__(self):
        #获取project id，每个project 一个 registry
        self.project_list = self.get_project_list()

        #获取 registry
        self.registry = CollectorRegistry()

        #获取 counter
        self.counter = Counter('sdg_ingestion_job_failed_times_total', 'Total failures of your job',
                               ['project_id', 'job_name','instance'], registry=self.registry)

        #获取job 列表 {project_id:[job_name,job_name,...],..}
        self.job_dic = self.get_job_name(self.project_list)

        self.log_file = open('sdg_ingestion_job_monitor.log','a')

    def get_project_list(self):
        '''获取项目 id 列表'''
        # 获取连接信息
        mysql_host = InnerConfigManager.get_instance().get_mysql_master()
        mysql_pass = InnerConfigManager.get_instance().get_client_conf('sp', 'mysql')['password']

        # 打开数据库连接
        db = pymysql.connect(host=mysql_host, user='work', password=mysql_pass, database='metadata', port=3305)

        # 获取游标对象
        cursor = db.cursor()
        # 获取 project_name
        sql = "select id from project"

        cursor.execute(sql)
        data = cursor.fetchall()

        # 关闭数据库连接
        db.close()
        result = []
        for i in data:
            if i[0]:
                result.append(i[0])

        return result

    def get_job_name(self,project_list):
        '''获取每个项目的指标名称'''
        # 获取连接信息
        mysql_host = InnerConfigManager.get_instance().get_mysql_master()
        mysql_pass = InnerConfigManager.get_instance().get_client_conf('sp', 'mysql')['password']

        # 打开数据库连接
        db = pymysql.connect(host=mysql_host, user='work', password=mysql_pass, database='metadata', port=3305)

        # 获取游标对象
        cursor = db.cursor()
        result = {}
        for project_id in project_list:
            # 获取 job_name
            sql = "select name from sdg_ingestion_table where project_id={}".format(project_id)

            cursor.execute(sql)
            data = cursor.fetchall()
            tmp = []
            for i in data:
                if i[0]:
                    tmp.append(i[0])
            result[project_id] = tmp

        # 关闭数据库连接
        db.close()
        return result

    def push_metric(self):
        while True:
            #更新job 列表
            self.job_dic = self.get_job_name(self.project_list)

            # 获取连接信息
            mysql_host = InnerConfigManager.get_instance().get_mysql_master()
            mysql_pass = InnerConfigManager.get_instance().get_client_conf('sp', 'mysql')['password']

            # 打开数据库连接
            db = pymysql.connect(host=mysql_host, user='work', password=mysql_pass, database='metadata', port=3305)

            # 获取游标对象
            cursor = db.cursor()

            for project_id, job_lst in self.job_dic.items() :
                if not job_lst:
                    continue

                for job_name in job_lst:
                    sql = "select job_status from sdg_ingestion_table where project_id={} and name='{}'".format(project_id,
                                                                                                                job_name)
                    cursor.execute(sql)
                    data = cursor.fetchone()
                    # 如果 job 的状态是 failure，对应的 counter inc
                    if data[0] and data[0] == 'failure':
                        self.counter.labels(project_id=project_id, job_name=job_name, instance='meta03').inc()

            push_to_gateway(MonitorSDGJob.pushgateway_address, job='sensors-inf-component-pushgateway',
                            registry=self.registry)
            db.close()
            #写日志
            with open('sdg_ingestion_job_monitor.log', 'a') as log_file:
                print(time.strftime('%Y%m%d-%H:%M:%S', time.localtime()), 'running', file=log_file)
                log_file.flush()

            #每上报一次指标 sleep 60s
            time.sleep(60)


if __name__ == '__main__':
    job = MonitorSDGJob()
    job.push_metric()





