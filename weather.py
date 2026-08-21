    def update(self, temperature):
        print("Temperature =", temperature, "°C")


# Subject Class
class WeatherStation:

    def __init__(self):
        self.display = []

    def register(self, obj):
        self.display.append(obj)

    def notify(self, temperature):
        for d in self.display:
            d.update(temperature)


# Main Program

d1 = Display()
d2 = Display()

station = WeatherStation()

station.register(d1)
station.register(d2)

station.notify(28)
station.notify(35)
