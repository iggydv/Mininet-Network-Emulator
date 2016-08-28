class Link():
    hostCount = 0
    def __init__(self, switch, host, bandwidth, loss, delay, jitter):
        self.bandwidth = bandwidth
        self.loss = loss
        self.delay = delay
        self.jitter = jitter
        self.switch = switch
        self.host = host
        

    def getBandwidth(self):
       return int(self.bandwidth)

    def getLoss(self):
       return int(self.loss)

    def getDelay(self):
       return self.delay

    def getJitter(self):
       return int(self.jitter)

    def getHost(self):
       return self.host

    def getSwitch(self):
       return self.switch
