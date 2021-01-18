from mininet.topo import Topo

class MyNet( Topo):
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
	self.addLink( First_Host, leftSwitch, bw=5)
	self.addLink( Second_Host, leftSwitch, bw=5)
	self.addLink( leftSwitch, rightSwitch, bw=1)
	self.addLink( Third_Host, rightSwitch, bw=5)
	self.addLink( Fourth_Host, rightSwitch, bw=5)

		

topos = { 'mytopo': ( lambda: MyNet() ) }
