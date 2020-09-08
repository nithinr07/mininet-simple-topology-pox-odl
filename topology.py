#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import random as rnd

def myNetwork(cont_ip):

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8',
		   link=TCLink)

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip=cont_ip,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, ip='10.0.0.12')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, ip='10.0.0.13')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, ip='10.0.0.14')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, ip='10.0.0.15')

    info( '*** Add hosts\n')
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)


    bw = [rnd.random()*(5-0) for x in range(14)]
    delay_rnd = [rnd.randint(2, 30) for x in range(14)]
    delay = [str(x)+'ms' for x in delay_rnd]
    info( '*** Add links\n')
    net.addLink(h2, s1, bw=bw[0], delay=delay[0])
    net.addLink(h1, s1, bw=bw[1], delay=delay[1])
    net.addLink(h4, s4, bw=bw[2], delay=delay[2])
    net.addLink(s4, h10, bw=bw[3], delay=delay[3])
    net.addLink(s4, h5, bw=bw[4], delay=delay[4])
    net.addLink(s4, h6, bw=bw[5], delay=delay[5])
    net.addLink(s3, h9, bw=bw[6], delay=delay[6])
    net.addLink(s3, h7, bw=bw[7], delay=delay[7])
    net.addLink(s2, s1, bw=bw[8], delay=delay[8])
    net.addLink(s2, s3, bw=bw[9], delay=delay[9])
    net.addLink(s3, s4, bw=bw[10], delay=delay[10])
    net.addLink(s1, h11, bw=bw[11], delay=delay[11])
    net.addLink(s1, h3, bw=bw[12], delay=delay[12])
    net.addLink(s3, h8, bw=bw[13], delay=delay[13])

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s3').start([c0])
    net.get('s4').start([c0])
    net.get('s2').start([c0])
    net.get('s1').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    pox = '127.0.0.1'
    odl = '192.168.56.104'
    controller = raw_input()
    if(controller == 'pox'):
    	myNetwork(pox)
    else:
	myNetwork(odl)

 
