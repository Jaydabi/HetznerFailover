# HetznerFailover
A simple class that handles failover ip address routing @Hetzner

## Example
```
failover = HetznerFailover('10.10.10.10', 'someuser', 'secret')`
failover.getActiveServer()
failover.setActiveServer('10.88.77.66')
```

getActiveServer() returns the ip of the server to which the failover ip is currently routed
setActiveServer() sets the ip of the server to which the failover ip should be routed
