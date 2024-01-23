'''
create_time: 2024/1/23 11:25
author: yss
version: 1.0
'''

import time
import pymysql
from prometheus_client import CollectorRegistry, Counter, push_to_gateway
from hyperion_client.hyperion_inner_client.inner_config_manager import InnerConfigManager


class MonitorSDGJob:
    # pushgateway_address = 'http://meta01.classic-ali-beijing-01.qimaoxiaoshuo.deploy.sensorsdata.cloud:8315'
    pushgateway_address = '10.130.13.32:8315'
    def __init__(self):
        #获取project id，每个project 一个 registry
        self.project_list = self.get_project_list()

        #获取 registry 列表
        self.registry = self.get_registry_list(self.project_list)

        #获取job 列表 {project_id:[],..}
        self.job_dic = self.get_job_name(self.project_list)

        #获取 counter 列表 {project_id:{job:counter,...}...}
        self.counter_dic = self.get_counter_name(self.job_dic)

    def get_registry_list(self,project_list):
        result = {}
        for project_id in project_list:
            result[project_id] = CollectorRegistry()
        return result

    def get_project_list(self):
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

    def get_counter_name(self,job_dic):
        result = {}
        for project_id,job_list in job_dic.items():
            if not job_list:
                continue
            tmp = {}
            for job in job_list:
                # 创建一个Counter指标
                job_failures = Counter(job, 'Total failures of your job',registry=self.registry[project_id])
                tmp[job] = job_failures
            result[project_id] = tmp
        return result

    def running(self,counter_dic):
        # print(self.project_list)
        # print(self.registry)
        # print(self.job_dic)
        # print(self.counter_dic)

        while True:
            # 获取连接信息
            mysql_host = InnerConfigManager.get_instance().get_mysql_master()
            mysql_pass = InnerConfigManager.get_instance().get_client_conf('sp', 'mysql')['password']

            # 打开数据库连接
            db = pymysql.connect(host=mysql_host, user='work', password=mysql_pass, database='metadata', port=3305)

            # 获取游标对象
            cursor = db.cursor()

            for project_id,counter_lst in counter_dic.items():
                if not counter_lst:
                    continue

                for job_name,counter in counter_lst.items():
                    sql = "select job_status from sdg_ingestion_table where project_id={} and name='{}'".format(project_id,job_name)
                    cursor.execute(sql)
                    data = cursor.fetchone()
                    #如果 job 的状态是 failure，对应的 counter inc
                    if data[0] and data[0] == 'failure':
                        counter.inc()


            #发送指标到 pushgateway
            for registry in self.registry.values():
                try:
                    push_to_gateway('10.130.13.32:8315', job='sdg_ingestion_job', registry=registry)
                except Exception as e:
                    print(e)
            db.close()
            print('run once')
            time.sleep(600)



if __name__ == '__main__':
    job = MonitorSDGJob()
    job.running(job.counter_dic)


