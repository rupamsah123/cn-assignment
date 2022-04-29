# RUPAM SAH
# CSB19029
from mininet.topo import Topo

class MyTopo(Topo):
	
	def build(self):
		HostList = []
		SwitchList = []
		
        
		for i in range(1,11):
			HostList.append(self.addHost("h{}".format(i)))
			SwitchList.append(self.addSwitch("s{}".format(i)))
			
        
		for i in range(1,11):
			for j in range(1,4):
				HostList.append(self.addHost("h{}{}".format(i,j)))


		for i in range(1,11):
				SwitchList.append(self.addSwitch("s{}{}".format(i,i)))

					
		for i in range(10):
			self.addLink(HostList[i],SwitchList[i])
			self.addLink(SwitchList[i],HostList[(i+1)%10])
			
		print(len(SwitchList))
		a = 10
		for i in range(10,20):
			self.addLink(SwitchList[i],HostList[a])
			self.addLink(SwitchList[i],HostList[a+1])
			self.addLink(SwitchList[i],HostList[a+2])
			a = a + 3
				
		self.addLink(SwitchList[4],SwitchList[14])
		
topos = {'topos' : (lambda : MyTopo())}