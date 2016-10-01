from NetworkEntity import *
from Host import *

class Switch(NetworkEntity):

    swCount = 0

    def __init__(self, bandwidth, loss, delay, jitter, hosts):

        self.bandwidth = bandwidth
        self.loss = loss
        self.delay = delay
        self.jitter = jitter
        Switch.swCount += 1
        self.switchname = 'S'+str(Switch.swCount)
        print("Switch '%s' created "%self.switchname)
        self.hosts = hosts

    def getBandwidth(self):
       return float(self.bandwidth)
    def getLoss(self):
        return float(self.loss)
    def getDelay(self):
        return self.delay
    def getJitter(self):
        return int(self.jitter)
    def getswitchname(self):
        return str(self.switchname)
    def getHost(self):
        return self.hosts
    
