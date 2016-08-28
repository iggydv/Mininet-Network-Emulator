from abc import ABCMeta, abstractmethod

class NetworkEntity(metaclass=ABCMeta):
        @abstractmethod
        def getBandwidth():
            pass

        @abstractmethod
        def getLoss():
            pass

        @abstractmethod
        def getDelay():
            pass

        @abstractmethod
        def getJitter():
            pass







