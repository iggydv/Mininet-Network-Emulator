import configparser
from Switch import *
from Host import *
from Link import *

# Add some comments explain to each method to explain their function
# See http://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format
class Parser():
    def __init__(self):
        global host_file, switch_file

        # This can be renamed to 'switches' - when naming variables, use plural to indicate that the
        # object is a list. Same goes for host_list and Link_list
        self.switch_list = []
        self.host_list = []
        # variables should start with lower case letters
        self.Link_list = []

    # The parse method should take the directory of the host and switch file, being able to
    # pass different files to the parser is essential for good design and testing.
    # eg. parse(self, hosts, switches)
    def parse(self):
        host_file = configparser.ConfigParser()
        # See comment above, this should be open(dir + 'hosts.txt')
        host_file.readfp(open('hosts.txt'))


        switch_file = configparser.ConfigParser()
        # Same comment as above
        switch_file.readfp(open('switches.txt'))
        
        for switches in switch_file.sections():
            # What happens if 'hosts' does not exists in the section?
            hosts = switch_file.get(switches, 'hosts')

            # The user might enter a string value, wrap your casting in a try...except
            # see http://stackoverflow.com/questions/5424716/python-how-to-check-if-input-is-a-number
            # Also, 10.5 is also a valid bandwidth, consider accepting floats as valid input
            # Also, I see you check if <0 - make sure mini net accepts bw, loss, delay and jitter equal to 0,
            # otherwise mininet might crash on input validated by the parser
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

        # Consider breaking the meat of the for loop into a method,
        # this will read easier and will be easier to debug:
        # for hosts in host_file.sections():
        #    host = translateSectionToHost(section)
        #    self.host_list.append(host)
        # Also, you have already defined 'hosts' in the previous loop
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

    # Methods names in python usually start with lower case with _ between words - eg. get_links
    def GetLinks(self):
        # If the switches list was called 'switches' you can name the iteration variable 'switch' (more descriptive than _s)
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
                            # this is a bit confusing, what is def_bw? If the host does not have spesific properties, it should inherit from the switch,
                            # so this makes more sense if bw = s_.getBandwidth()
                            # Also, you can roll this into a one liner:
                            # bw = switch.getBandwidth() if current_host.getBandwidth() is None else current_host.getBandwidth()
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

        # Validation should not happen in the getters of this class - that is what the parse method is for.
        # Change you parse method up, read the hosts first, and then the switches. When parsing a switch,
        # go through all the defined hosts and do a lookup in the host list, if the host does not exist,
        # raise and exception and say that switch xyz is malformed
        if found == 0:
            raise ValueError('Host '+h_+ ' does not exist\n')
            quit()
        return self.Link_list
        

    def GetHosts(self):
        return self.host_list

    def GetSwitches(self):
        return self.switch_list

        
        
