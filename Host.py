from NetworkEntity import *

class Host(NetworkEntity):
    hostCount = 0
    # Each host needs a name. This will be easier to identify each host. The name of the\\
    # host can be define as the section name of the host file - keeping count makes little sense
    def __init__(self, bandwidth, loss, delay, jitter):
        self.bandwidth = bandwidth
        self.loss = loss
        self.delay = delay
        self.jitter = jitter
        Host.hostCount +=1
        self.hostname = "h"+str(Host.hostCount)
        print("Host '%s' created "%self.hostname)

    def getBandwidth(self):
       return int(self.bandwidth)

    def getLoss(self):
       return int(self.loss)

    def getDelay(self):
       return self.delay

    def getJitter(self):
       return int(self.jitter)

    def getHostName(self):
       return self.hostname

