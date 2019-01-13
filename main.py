# -*- coding:utf-8 -*-
#python3.6
import pyserial



connection = 1



class fixture:
    def __init__(self, name, testname=None, robotname=None):
        #like cell45
        self.name = name
        #like rf42w7cell1 ,it associate with test cell name or connections with product console
        self.testname = name
        #like fix1, it associate with the position
        self.robotname = robotname

    def add_serial(self, parameter_list):
        #'open serial connection to fixture'
        self.con ='a serial connection object'

    def get_state(self, command='state',timeout=5):
        '''
        send command "state" to get the status of fixture, in general, there are 3 states
        return a tuple(fixture_state, if exist product)
        '''
        self.con.send(command=command, timeout=timeout)
        if 'OK' in self.connection.recbuffer:
            return ('OPEN','PD')
        elif 'NOT PRO' in self.connection.recbuffer:
            return ('OPEN','NOT PD')
        return ('ERROR','ERROR')

    def open_fix(self):
        self.con.send(command='OPEN', expected='OPEN_OK', timeout=5)

    def close_fix(self):
        self.con.send(command='CLOSE', expected='CLOSE_OK', timeout=5)

class testcell:
    #just for get states of testcell 
    def __init__(self, name):
        self.name = name
    def get_state(self):
        self.state = 'PASS'







    
        

