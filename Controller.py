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
    
    global switch_list
    switch_list = []

    global host_list
    host_list = []
    
    global link_list
    link_list = []

    def __init__( self ):
        Topo.__init__(self)
        Dir = '/home/mininet/skripsie'
        parser = Parser(Dir)
        parser.parse()

        host_list = parser.GetHosts()
        switch_list = parser.GetSwitches()
        link_list = parser.GetLinks()

        for host in host_list:
            self.addHost(host.getHostName())

        for switch in switch_list:
            self.addSwitch(switch.getswitchname())

        for links in link_list:
            self.addLinks(links.getSwitch(),links.getHost(),bw = links.getBandwidth(),loss = links.getLoss(),delay = links.getDelay())
        

topos = { 'mytopo': ( lambda: Controller() ) }

    
        

