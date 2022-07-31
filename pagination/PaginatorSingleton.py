import pandas
from django.core import paginator
from django.core.paginator import Paginator

from pagination import settings

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class PaginatorSingleton(metaclass=MetaSingleton):
    paginator = None

    def getPaginator(self):
        if self.paginator is None:
            self.paginator = Paginator(self.read_file(), 10)
        return self.paginator

    @staticmethod
    def read_file():
        #Есть смысл подгружать последующие страницы по мере листания
        x = pandas.read_csv(settings.BUS_STATION_CSV, skiprows=0, nrows=1000)
        bus_stations = []
        for i in range(1000):
            station = {}
            station['Name'] = x.loc[i].at["Name"]
            station['Street'] = x.loc[i].at["Street"]
            station['District'] = x.loc[i].at["District"]
            bus_stations.append(station)
        return bus_stations
