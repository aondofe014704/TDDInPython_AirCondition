from unittest import TestCase

from assignment_in_python.air_condition import AirCondition


class AirConditionTest(TestCase):

    def test_airCondition_can_be_turned_on(self):
        airCondition = AirCondition()
        airCondition.turnOff()
        self.assertTrue(airCondition.turnOff())
        airCondition.turnOn()
        self.assertTrue(airCondition.turnOn())

    def test_airCondition_can_be_turned_off(self):
        airCondition = AirCondition()
        airCondition.turnOn()
        self.assertTrue(airCondition.turnOn())
        airCondition.turnOff()
        self.assertTrue(airCondition.turnOff())

    def test_increase_temperature_increased(self):
        airCondition = AirCondition()
        airCondition.turnOn()
        airCondition.increaseTemperature()
        self.assertEqual(17, airCondition.temperature)

    def test_decrease_temperature_decreased(self):
        airCondition = AirCondition()
        airCondition.decreaseTemperature()
        self.assertEqual(15, airCondition.temperature)

    def test_that_temperature_cannot_be_increased_above_Thirty(self):
        airCondition = AirCondition()
        self.assertEqual(17, airCondition.increaseTemperature())

