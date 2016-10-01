from NetworkEntity import *

class Host(NetworkEntity):
    
    def __init__(self, hostname, bandwidth, loss, delay, jitter):
        self.bandwidth = bandwidth
        self.loss = loss
        self.delay = delay
        self.jitter = jitter
        self.hostname = hostname

    def getBandwidth(self):
       return float(self.bandwidth)

    def getLoss(self):
       return float(self.loss)

    def getDelay(self):
       return self.delay

    def getJitter(self):
       return int(self.jitter)

    def getHostName(self):
       return self.hostname

