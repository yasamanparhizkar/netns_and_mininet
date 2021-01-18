from mininet.topo import Topo

class MyNet( Topo ):
    "Section 3 Topology"

    def __init__( self ):
 	# Initialize topology
        Topo.__init__( self )

	# Add hosts and switches
	First_Host = self.addHost( 'h1' )
	Second_Host = self.addHost( 'h2' )
	Third_Host = self.addHost( 'h3' )
	Fourth_Host = self.addHost( 'h4' )
	leftSwitch = self.addSwitch( 's1' )
	rightSwitch = self.addSwitch( 's2' )

	# Add links
	self.addLink( First_Host, leftSwitch, delay='20ms')
	self.addLink( Second_Host, leftSwitch, delay='20ms')
	self.addLink( leftSwitch, rightSwitch, delay='50ms')
	self.addLink( Third_Host, rightSwitch, delay='15ms')
	self.addLink( Fourth_Host, rightSwitch, delay='1s')
		

topos = { 'mytopo': ( lambda: MyNet() ) }


