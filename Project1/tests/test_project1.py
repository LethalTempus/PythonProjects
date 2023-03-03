import unittest, contextlib, io
from pathlib import Path
from project1 import *

class TestDeviceCommunication(unittest.TestCase):
    def test_device_creation(self):
        A = Device("1")
        self.assertEqual(A.device_name, "1")

    def test_store_propagation_info(self):
        A = Device("1")
        A.store_propagation_info([("1", "2", "700"), ("2", "3", "500")])
        self.assertEqual([("1", "2", "700")], A.propagation_info_list)

    def test_alert_cancel_info(self):
        A = Device("1")
        A.store_alert_cancel_info([["ALERT","1","Trouble","0"],["CANCEL","1","Trouble","2200"]])
        self.assertEqual([["ALERT","1","Trouble","0"],["CANCEL","1","Trouble","2200"]], A.alert_cancel_info_list)

    def test_alert_cancel_info_1(self):
        A = Device("2")
        A.store_alert_cancel_info([["ALERT","1","Trouble","0"],["CANCEL","1","Trouble","2200"]])
        self.assertEqual([], A.alert_cancel_info_list)

    def test_check_for_event(self):
        A = Device("1")
        A.store_propagation_info([("1", "2", "700"), ("2", "3", "500")])
        A.store_alert_cancel_info([["ALERT", "1", "Trouble", "0"], ["CANCEL", "1", "Trouble", "2200"]])
        Device.time_count = 0
        P_list = A.check_for_event()
        self.assertEqual([0, 'ALERT', 'Trouble', '1', '', 0], P_list)

    def test_check_for_event_1(self):
        A = Device("2")
        A.store_propagation_info([("1", "2", "700"), ("2", "3", "500"),("3", "2", "1000")])
        A.store_alert_cancel_info([["ALERT", "1", "Trouble", "0"], ["CANCEL", "1", "Trouble", "2200"]])
        Device.time_count = 0
        P_list = A.check_for_event()
        self.assertEqual([], P_list)


    def test_check_if_send(self):
        A = Device("1")
        A.store_propagation_info([("1", "2", "700"), ("2", "3", "500")])
        A.store_alert_cancel_info([["ALERT", "1", "Trouble", "0"], ["CANCEL", "1", "Trouble", "2200"]])
        Device.time_count = 0
        P_list = [0, 'ALERT', 'Trouble', '1', '', 0]
        A.check_if_send(P_list)
        self.assertEqual(Device.packet_list_1, [700, 'ALERT', 'Trouble', '2', '', 0])

    def test_check_if_send_1(self):
        A = Device("1")
        A.store_propagation_info([("1", "2", "700"), ("2", "3", "500")])
        A.store_alert_cancel_info([["ALERT", "1", "Trouble", "0"], ["CANCEL", "1", "Trouble", "2200"]])
        Device.time_count = 2200
        P_list = [2200, 'CANCEL', 'Trouble', '1', '', 0]
        A.check_if_send(P_list)
        self.assertEqual(Device.packet_list_1, [2900, 'CANCEL', 'Trouble', '2', '', 0])

    def test_check_if_send_2(self):
        B = Device("3")
        B.store_propagation_info([("3", "2", "700"), ("3", "4", "500")])
        B.store_alert_cancel_info([["ALERT", "1", "Trouble", "0"], ["CANCEL", "1", "Trouble", "2200"]])
        Device.time_count = 2200
        P_list = [2200, 'CANCEL', 'Trouble', '1', '', 0]
        B.check_if_send(P_list)
        self.assertEqual(Device.packet_list_1, [2900, 'CANCEL', 'Trouble', '2', '', 0])
