HetznerFailover
=====

A simple class that handles failover ip address routing @Hetzner

Usage Example
-------

failover = HetznerFailover('10.10.10.10', 'hetznerLogin', 'hetznerPassword')
failover.getActiveServer()
failover.setActiveServer('10.99.88.77')
