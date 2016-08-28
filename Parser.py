import configparser
from Switch import *
from Host import *
from Link import *

class Parser():
    def __init__(self):
        global host_file, switch_file
        
        self.switch_list = []
        self.host_list = []
        self.Link_list = []
        
    def parse(self):
        host_file = configparser.ConfigParser()
        host_file.readfp(open('hosts.txt'))
        

        switch_file = configparser.ConfigParser()
        switch_file.readfp(open('switches.txt'))
        
        for switches in switch_file.sections():
            hosts = switch_file.get(switches, 'hosts')
            
            def_bw = int(switch_file.get(switches, 'bw'))
            if def_bw and (def_bw <0 or def_bw > 1000):
                raise ValueError('Bandwidth ',def_bw, 'is outside range 0...1000 Mbps\n')

            def_loss = int(switch_file.get(switches, 'loss'))
            if def_loss and (def_loss <0 or def_loss > 100):
                raise ValueError('Loss ',def_loss, 'is outside range 0...100 %\n')

            def_delay = switch_file.get(switches, 'delay')+'ms' 
            def_delay_ = int(switch_file.get(switches, 'delay'))
            if def_delay_ and (def_delay_ <0 or def_delay_ > 1000):
                raise ValueError('Delay ',def_delay_, 'is outside range 0...1000 ms\n')

            def_jitter = int(switch_file.get(switches, 'jitter'))
            if def_jitter and (def_jitter <0 or def_jitter > 1000):
                raise ValueError('Jitter ',def_jitter, 'is outside range 0...100\n')

            s = Switch(def_bw, def_loss, def_delay, def_jitter, hosts)
            self.switch_list.append(s)
            print("Adding section "+s.getswitchname())

        for hosts in host_file.sections():
                bw = int(host_file.get(hosts, 'bw'))
                if bw and (bw <0 or bw > 1000):
                    raise ValueError('Bandwidth ',bw, 'is outside range 0...1000 Mbps\n')

                loss = int(host_file.get(hosts, 'loss'))
                if loss and (loss <0 or loss > 100):
                    raise ValueError('Loss ',loss, 'is outside range 0...100 %\n')

                delay = host_file.get(hosts, 'delay')+'ms'   
                delay_ = int(host_file.get(hosts, 'delay'))
                if delay_ and (delay_ <0 or delay_ > 1000):
                    raise ValueError('Delay ',delay_, 'is outside range 0...1000 ms\n')

                jitter = int(host_file.get(hosts, 'jitter'))
                if def_jitter and (jitter <0 or jitter > 1000):
                    raise ValueError('Jitter ',jitter, 'is outside range 0...100\n')
                h = Host(bw, loss, delay, jitter)
                self.host_list.append(h)
                
        print("\n...all hosts and Switches created...\n")
        return
    
    def GetLinks(self):
        for s_ in self.switch_list:
            hosts = s_.hosts.split(',')
            print('Requested links:')
            print(hosts)
            for host in hosts:
                found = 0
                h_ = host.strip()
                for current_host in self.host_list:
                    if h_ == current_host.getHostName():
                            
                        found = 1
                        bw = current_host.getBandwidth()
                        if bw == None:
                            bw = int(def_bw)


                        loss = current_host.getLoss()
                        if loss == None:
                            loss = int(def_loss)


                        delay = current_host.getDelay()
                        if delay == None:
                            delay = def_delay
                            


                        jitter = current_host.getJitter()
                        if jitter == None:
                            jitter = def_jitter
                        print("alright i'm creating the links now: %s -> %s (%d Mbps %d percent %s )"%(s_.getswitchname(),h_, bw, loss, delay))
                        l = Link(s_.getswitchname(),h_, bw, loss, delay, jitter)
                        self.Link_list.append(l)
                        
        if found == 0:
            raise ValueError('Host '+h_+ ' does not exist\n')
            quit()
        return self.Link_list
        

    def GetHosts(self):
        return self.host_list

    def GetSwitches(self):
        return self.switch_list

        
        
