# HetznerFailover
A simple class that handles failover ip address routing @Hetzner

## Example
```
failover = HetznerFailover('10.10.10.10', 'hetznerApiUsername', 'hetznerApiPassword')`
failover.getActiveServer()
failover.setActiveServer('10.88.77.66')
```
