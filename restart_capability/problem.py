import json
import requests
from collections import deque


class My_exception(Exception):
    def __init(self, msg):
        self.msg = msg


class Db_Delete(object):
    def __init__(self):
        pass

    def one(self):
        pass

    def two(self):
        pass
    def three(self):
        pass
    def four(self):
        pass
    def five(self):
        pass

    def six(self):
        pass

    def seven(self):
        pass

    def go(self, first_run):
        if first_run:
            print "build queue"
            my_q = deque([])
            my_q.append(self.one)
            my_q.append(self.two)
            my_q.append(self.three)
            my_q.append(self.four)
            my_q.append(self.five)
            my_q.append(self.six)
            my_q.append(self.seven)
            try:
                my_stack = deque([])
                for i in range(7):
                    my_q.popleft()()
            except My_exception as e:
                print "build my stack"
                while len(my_q) > 0: 
                    my_stack.append(my_q.pop())
                my_stack.append(e.message['name'])
                print list(my_stack)
                
        else:
            print "second run (restart)" 
            print "get stack from mongo "
            my_stack = deque([self.four, self.five, self.six, self.seven])
            try:
                while len(my_stack) > 0:
                    my_stack.popleft()()
            except My_exception as e:
                if len(my_stack) > 0:
                    my_stack.appendleft(e.message['name'])
                print list(my_stack)
            
                
            

class Mg(Db_Delete):
    def one(self):

        headers = {
            'Authorization': 'Basic Q0RCX1Rlc2xhLmdlbjpEMG50X2Nobmcz',
            'Content-Type': 'application/json',
            }

        data = '{"cluster_name":"csdb02npd"}'

        response = requests.post('https://cdb-jmp-dev3-001:8020/api/v1/cdb/cassandra/generic/get_cluster_details', headers=headers, data=data, verify=False)
        res =  json.loads(response.content)
        if res['Status'] == "Provisioned":
            return 0
        else:
            msg = {"status": "Failed", "name": "self.one"}
            raise My_exception(msg)
        

    def two(self):
        headers = {
            'Authorization': 'Basic Q0RCX1Rlc2xhLmdlbjpEMG50X2Nobmcz',
            'Content-Type': 'application/json',
            }

        data = '{"cluster_name":"csdb02npd"}'

        response = requests.post('https://cdb-jmp-dev3-001:8020/api/v1/cdb/cassandra/generic/get_cluster_details', headers=headers, data=data, verify=False)
        res =  json.loads(response.content)
        if res['Status'] == "Provisioned":
            return 0
        else:
            msg = {"status": "Failed", "name": "self.two"}
            raise My_exception(msg)

    def three(self):
        headers = {
            'Authorization': 'Basic Q0RCX1Rlc2xhLmdlbjpEMG50X2Nobmcz',
            'Content-Type': 'application/json',
            }

        data = '{"cluster_name":"csdb02npd"}'

        response = requests.post('https://cdb-jmp-dev3-001:8020/api/v1/cdb/cassandra/generic/get_cluster_details', headers=headers, data=data, verify=False)
        res =  json.loads(response.content)
        if res['Status'] == "Provisioned":
            return 0
        else:
            msg = {"status": "Failed", "name": "self.three"}
            raise My_exception(msg)

    def four(self):
        headers = {
            'Authorization': 'Basic Q0RCX1Rlc2xhLmdlbjpEMG50X2Nobmcz',
            'Content-Type': 'application/json',
            }

        data = '{"cluster_name":"csdb02npd"}'

        response = requests.post('https://cdb-jmp-dev3-001:8020/api/v1/cdb/cassandra/generic/get_cluster_details', headers=headers, data=data, verify=False)
        res =  json.loads(response.content)
        if res['Status'] == "Provisione":
            return 0
        else:
            msg = {"status": "Failed", "name": "self.four"}
            raise My_exception(msg)
        print "abhishake to implement"

    def five(self):
        headers = {
            'Authorization': 'Basic Q0RCX1Rlc2xhLmdlbjpEMG50X2Nobmcz',
            'Content-Type': 'application/json',
            }

        data = '{"cluster_name":"csdb02npd"}'

        response = requests.post('https://cdb-jmp-dev3-001:8020/api/v1/cdb/cassandra/generic/get_cluster_details', headers=headers, data=data, verify=False)
        res =  json.loads(response.content)
        if res['Status'] == "Provisioned":
            return 0
        else:
            msg = {"status": "Failed", "name": "self.five"}
            raise My_exception(msg)
        print "abhishake to implement"

    def six(self):
        headers = {
            'Authorization': 'Basic Q0RCX1Rlc2xhLmdlbjpEMG50X2Nobmcz',
            'Content-Type': 'application/json',
            }

        data = '{"cluster_name":"csdb02npd"}'

        response = requests.post('https://cdb-jmp-dev3-001:8020/api/v1/cdb/cassandra/generic/get_cluster_details', headers=headers, data=data, verify=False)
        res =  json.loads(response.content)
        if res['Status'] == "Provisioned":
            return 0
        else:
            msg = {"status": "Failed", "name": "self.six"}
            raise My_exception(msg)
        print "abhishake to implement"

    def seven(self):
        headers = {
            'Authorization': 'Basic Q0RCX1Rlc2xhLmdlbjpEMG50X2Nobmcz',
            'Content-Type': 'application/json',
            }

        data = '{"cluster_name":"csdb02npd"}'

        response = requests.post('https://cdb-jmp-dev3-001:8020/api/v1/cdb/cassandra/generic/get_cluster_details', headers=headers, data=data, verify=False)
        res =  json.loads(response.content)
        if res['Status'] == "Provisioned":
            return 0
        else:
            msg = {"status": "Failed", "name": "self.seven"}
            raise My_exception(msg)
        print "abhishake to implement"


class Cs(Db_Delete):
    def one(self):
        print "to implement"

    def two(self):
        print "to implement"
    def three(self):

        print "to implement"
    def four(self):
        print "to implement"

    def five(self):
        print "to implement"

    def six(self):
        print "to implement"

    def seven(self):
        print "to implement"

obj = Mg()
obj.go(False)
