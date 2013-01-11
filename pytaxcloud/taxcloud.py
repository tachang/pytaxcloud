from suds.client import Client
from decimal import *

class TaxCloud:

  def __init__(self, api_login_id, api_key):
    self.api_login_id = api_login_id
    self.api_key = api_key
    self.soap_url = 'https://api.taxcloud.net/1.0/TaxCloud.asmx'
    self.wsdl_url = 'https://api.taxcloud.net/1.0/?wsdl' 

    self.client = Client(url=wsdl_url, location=soap_url)


  def lookup():
    pass



address = client.factory.create('Address')
address.Address1 = "150 Dolores St"
address.Address2 = ""
address.City = "San Francisco"
address.State = "CA"
address.Zip5 = "94103"

cart_items = client.factory.create('ArrayOfCartItem')
print cart_items


cart_item = client.factory.create('CartItem')

print cart_item

cart_item.Index = 1
cart_item.ItemID = 1
cart_item.TIC = 0
cart_item.Price = Decimal("100.00")
cart_item.Qty = 1

cart_items.CartItem = [cart_item]


print client.service.Lookup(api_login_id,
                            api_key,
                            "customerid",
                            "cartid",
                            cart_items,
                            address,
                            address,
                            False,
                            None)
"""

"""
Lookup(xs:string apiLoginID, xs:string apiKey, xs:string customerID, xs:string cartID, ArrayOfCartItem cartItems,
Address origin,
Address destination,
xs:boolean deliveredBySeller,
ExemptionCertificate exemptCert, )

"""
