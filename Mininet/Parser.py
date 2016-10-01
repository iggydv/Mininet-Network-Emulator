import configparser
from Switch import *
from Host import *
from Link import *

class Parser():
    def __init__(self, Dir):
        global host_file, switch_file, topo_file
        self.Dir = Dir
        self.topology = ''
        self.prev_switch = ''
        self.switches = []
        self.hosts = []
        self.links = []
        
    def parse(self):
        print("The Parser Class is now starting")
        #This function is used to instantiate all switch and host objects
        #which are used to easily access information about the specific switch or host
        #which is then passed to mininet

        
        host_file = configparser.ConfigParser()
        host_file.readfp(open(self.Dir+'/hosts2.txt'))
        

        switch_file = configparser.ConfigParser()
        switch_file.readfp(open(self.Dir+'/switches2.txt'))

        topo_file = open(self.Dir+'TopoType.txt','r')
        self.topology = topo_file.readline()
        topo_file.close()
        
        
        for switch in switch_file.sections():
            hosts = switch_file.get(switch, 'hosts')
            
            def_bw = float(switch_file.get(switch, 'bw'))
            if def_bw and (def_bw <0 or def_bw > 1000):
                raise ValueError('Bandwidth ',def_bw, 'is outside range 0...1000 Mbps\n')

            def_loss = float(switch_file.get(switch, 'loss'))
            if def_loss and (def_loss <0 or def_loss > 100):
                raise ValueError('Loss ',def_loss, 'is outside range 0...100 %\n')

            def_delay = switch_file.get(switch, 'delay')+'ms' 
            def_delay_ = float(switch_file.get(switch, 'delay'))
            if def_delay_ and (def_delay_ <0 or def_delay_ > 1000):
                raise ValueError('Delay ',def_delay_, 'is outside range 0...1000 ms\n')

            def_jitter = float(switch_file.get(switch, 'jitter'))
            if def_jitter and (def_jitter <0 or def_jitter > 1000):
                raise ValueError('Jitter ',def_jitter, 'is outside range 0...100\n')

            s = Switch(def_bw, def_loss, def_delay, def_jitter, hosts)
            self.switches.append(s)
            print("Adding section "+s.getswitchname())

        for host in host_file.sections():
                print("Adding host: %s"%host)
                bw = float(host_file.get(host, 'bw'))
                if bw and (bw <0 or bw > 1000):
                    raise ValueError('Bandwidth ',bw, 'is outside range 0...1000 Mbps\n')

                loss = float(host_file.get(host, 'loss'))
                if loss and (loss <0 or loss > 100):
                    raise ValueError('Loss ',loss, 'is outside range 0...100 %\n')

                delay = host_file.get(host, 'delay')+'ms'   
                delay_ = float(host_file.get(host, 'delay'))
                if delay_ and (delay_ <0 or delay_ > 1000):
                    raise ValueError('Delay ',delay_, 'is outside range 0...1000 ms\n')

                jitter = float(host_file.get(host, 'jitter'))
                if def_jitter and (jitter <0 or jitter > 1000):
                    raise ValueError('Jitter ',jitter, 'is outside range 0...100\n')
                h = Host(host, bw, loss, delay, jitter)
                self.hosts.append(h)
                
        print("\n...all hosts and Switches created...\n")
        return
    
    def get_Links(self):
        # In order to create links between network entities, this function creates
        # link objects which is used to identify which entities are connected to one another
        # and to return a list of Link objects
        c = 0
        for switch in self.switches:
            c +=1
            print('in Here')
            hosts = switch.hosts.split(',')
            print('Requested links:')
            print(hosts)
            for host in hosts:
                found = 0
                h_ = host.strip()
                
                for current_host in self.hosts:
                    if h_ == current_host.getHostName():
                        found = 1
                        bw = switch.getBandwidth() if current_host.getBandwidth() is None else current_host.getBandwidth()
                        loss = switch.getLoss() if current_host.getLoss() is None else current_host.getLoss()
                        delay = switch.getDelay() if current_host.getDelay() is None else current_host.getDelay()
                        jitter = switch.getJitter() if current_host.getJitter() is None else current_host.getJitter()
                        print("Creating Link: %s -> %s (%.2f Mbps %d percent %s )"%(switch.getswitchname(),h_, bw, loss, delay))
                        l = Link(switch.getswitchname(),h_, bw, loss, delay, jitter)
                        self.links.append(l)
            if c > 1:
                l = Link(switch.getswitchname(),self.prev_switch.getswitchname(), 0, 0, 0, 0)
                print("Creating Link: %s -> %s (%.2f Mbps %d percent %s )"%(switch.getswitchname(),self.prev_switch.getswitchname(), bw, loss, delay))
            self.prev_switch = switch
              
        if found == 0:
            raise ValueError('Host '+h_+ ' does not exist\n')
            quit()
            
        return self.links
        

    def get_Hosts(self):
        #return a list of Host objects
        return self.hosts

    def get_Switches(self):
        #return a list of Switch objects
        return self.switches
    def get_Topo(self):
        return self.topology



parser = Parser('D:/WinPython-64bit-3.4.3.7/MyWork/Skripsie/ig/')
parser.parse()
links = parser.get_Links()

        
        
