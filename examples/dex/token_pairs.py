from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCDecentralizedExchange")
dex = MoCDecentralizedExchange(connection_manager)
print(dex.token_pairs())

#pair = ['0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0', '0x840871cbb73dC94dcb11b2CEA963553Db71a95b7']
#print(dex.token_pairs_status(pair[0], pair[1]))

"""
[['0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0', '0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf'], 
['0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0', '0xA274d994F698Dd09256674960d86aBa22C086669'],
 ['0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0', '0x19F64674D8A5B4E652319F5e239eFd3bc969A1fE']]

"""