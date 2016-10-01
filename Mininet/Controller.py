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
    
    def __init__( self, Dir ):
        Topo.__init__(self)
        parser = Parser(Dir)
        parser.parse()
        
        hosts = parser.get_Hosts()
        switchs = parser.get_Switches()
        links = parser.get_Links()

        for host in hosts:
            self.addHost(host.getHostName())

        for switch in switches:
            self.addSwitch(switch.getswitchname())

        for link in links:
            self.addLink(link.getSwitch(),link.getHost(),bw = link.getBandwidth(),loss = link.getLoss(),delay = link.getDelay(), jitter = links.getJitter())
            

topos = { 'mytopo': ( lambda: Controller('./topo1') ) }

    
        

