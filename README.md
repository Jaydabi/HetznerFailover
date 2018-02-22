# HetznerFailover
A simple class that handles failover ip address routing @Hetzner

## Example
```
failover = HetznerFailover('10.10.10.10', 'someuser', 'secret')`
failover.getActiveServer()
failover.setActiveServer('10.88.77.66')
```

### HetznerFailover(failoverIp, login, password)
returns nothing

### getActiveServer()
requires no argument

returns the ip of the server to which the failover ip is currently routed

### setActiveServer(ip)
requires ip of the new routing target

sets the ip of the server to which the failover ip should be routed

returns True on success, otherwise False
