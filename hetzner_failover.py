import requests
import json

class HetznerFailover():
    
    def __init__(self,failoverIp,login,password):
        self.failoverIp = failoverIp
        self.login = login
        self.password = password
        
    def getActiveServer(self):
        response = requests.get('https://robot-ws.your-server.de/failover/{}'.format(self.failoverIp), auth=(self.login,self.password))
        responseContent = json.loads(response.content.decode())
        if response.status_code == 401 or response.status_code == 404:
            raise RuntimeError('{}: {}'.format(responseContent['error']['code'],responseContent['error']['message']))
        return responseContent['failover']['active_server_ip']
        
    def setActiveServer(self, ip):
        response = requests.post('https://robot-ws.your-server.de/failover/{}'.format(self.failoverIp), auth=(self.login,self.password), data={'active_server_ip': '{}'.format(ip)})
        responseContent = json.loads(response.content.decode())
        if response.status_code == 400 or response.status_code == 401 or response.status_code == 404 or response.status_code == 500:
            raise RuntimeError('{}: {}'.format(responseContent['error']['code'],responseContent['error']['message']))
        elif response.status_code == 409:
            if responseContent['error']['code'] == 'FAILOVER_LOCKED':
                raise RuntimeError('{}: {}'.format(responseContent['error']['code'],responseContent['error']['message']))
            elif responseContent['error']['code'] == 'FAILOVER_ALREADY_ROUTED':
                return True
        if responseContent['failover']['active_server_ip'] == ip:
            return True
        else:
            return False
