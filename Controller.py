import sys, os
sys.path.append('/home/mininet/skripsie')
import ConfigParser
from Parser import *
from Switch import *
from Host import *
from Link import *
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import CPULimitedHost
from mininet.link import TCLink


class Controller( Topo ):

    # this is redundant as you define it in the __init__ method
    global switch_list
    switch_list = []

    global host_list
    host_list = []
    
    global link_list
    link_list = []

    # add a parameter to define the dir
    # like __init__(self, dir)
    def __init__( self ):
        Topo.__init__(self)
        # do not hard code the dir of the config
        Dir = '/home/mininet/skripsie'
        # Parser should
        parser = Parser(Dir)
        parser.parse()

        # Rather call this hosts = ... and switches = ...
        host_list = parser.GetHosts()
        switch_list = parser.GetSwitches()
        link_list = parser.GetLinks()

        #This is nice and clean, well done
        for host in host_list:
            self.addHost(host.getHostName())

        for switch in switch_list:
            self.addSwitch(switch.getswitchname())

        # naming - 'for link in links:' makes more sense
        for links in link_list:
            self.addLinks(links.getSwitch(),links.getHost(),bw = links.getBandwidth(),loss = links.getLoss(),delay = links.getDelay())
        

# If you can pass the dir of config to the controller, you can easily set up different topos,
# eg, topos = {'mytopo': ( lambda: Controller('path/to/topo/one') ), 'mysecondtopo': ( lambda: Controller('path/to/my/second/controlelr') )}
# I believe you would be able to call the topo by name when launching mini net if it is in this dict of topos
topos = { 'mytopo': ( lambda: Controller() ) }

    
        

