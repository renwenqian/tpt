"""Custom topology example

Two directly connected switches plus a host for each switch:

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        RootSwitch = self.addSwitch( 's1' )
        FirstleftSwitch = self.addSwitch( 's2' )
        FirstrightSwitch = self.addSwitch( 's3' )
        SecondleftSwitch = self.addSwitch( 's4' )
        SecondrightSwitch = self.addSwitch( 's5' )
        SecondsleftSwitch = self.addSwitch( 's6' )
        SecondsrightSwitch = self.addSwitch( 's7' )
        FirstHost = self.addHost( 'h1' )
        SecondHost = self.addHost( 'h2' )
        ThirdHost = self.addHost( 'h3' )
        FourthHost = self.addHost( 'h4' )
        FifthHost = self.addHost( 'h5' )
        SixthHost = self.addHost( 'h6' )
        SeventhHost = self.addHost( 'h7' )
        EighthHost = self.addHost( 'h8' )

        # Add links
        self.addLink( RootSwitch, FirstleftSwitch )
        self.addLink( RootSwitch, FirstrightSwitch )
        self.addLink( FirstleftSwitch, SecondleftSwitch )
        self.addLink( FirstleftSwitch, SecondrightSwitch )
        self.addLink( FirstrightSwitch, SecondsleftSwitch )
        self.addLink( FirstrightSwitch, SecondsrightSwitch )
        self.addLink( SecondleftSwitch, FirstHost )
        self.addLink( SecondleftSwitch, SecondHost )
        self.addLink( SecondrightSwitch, ThirdHost )
        self.addLink( SecondrightSwitch, FourthHost )
        self.addLink( SecondsleftSwitch, FifthHost )
        self.addLink( SecondsleftSwitch, SixthHost )
        self.addLink( SecondsrightSwitch, SeventhHost )
        self.addLink( SecondsrightSwitch, EighthHost )



topos = { 'mytopo': ( lambda: MyTopo() ) }
