from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink

class MyNet( Topo ):
    "Section 3 Topology"

    def __init__( self ):
 	# Initialize topology
	Topo.__init__( self )

	# Add hosts and switches
	First_Host = self.addHost( 'h1' )
	Second_Host = self.addHost( 'h2' )
	leftSwitch = self.addSwitch( 's1' )
	rightSwitch = self.addSwitch( 's2' )


	# Add links
	self.addLink( First_Host, leftSwitch, bw=1, delay='1s', max_queue_size = 100)
	self.addLink( leftSwitch, rightSwitch, bw=1, delay='1s', max_queue_size = 100)
	self.addLink( Second_Host, rightSwitch, bw=1, delay='1s', max_queue_size = 100)
		

topos = { 'mytopo': ( lambda: MyNet() ) }

