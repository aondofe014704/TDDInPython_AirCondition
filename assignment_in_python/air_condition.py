class AirCondition:
    def __init__(self):
        self.isOn = False
        self.temperature = 16

    def turnOn(self):
        result = self.isOn = True
        return result

    def turnOff(self):
        result = self.isOn = True
        return result

    def increaseTemperature(self):
        self.temperature = self.temperature + 1
        return self.temperature

    def decreaseTemperature(self):
        self.temperature = self.temperature - 1
        return self.temperature
