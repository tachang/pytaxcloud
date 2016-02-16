from suds.client import Client
from decimal import *


class TaxCloudException(Exception):
  pass

class TaxCloud:

  def __init__(self, api_login_id, api_key):
    self.api_login_id = api_login_id
    self.api_key = api_key
    self.soap_url = 'https://api.taxcloud.net/1.0/TaxCloud.asmx'
    self.wsdl_url = 'https://api.taxcloud.net/1.0/?wsdl' 

    self.client = Client(url=self.wsdl_url, location=self.soap_url)

  def convertToAddress(self, data):

    address = self.client.factory.create('Address')
    address.Address1 = data['address1']
    address.Address2 = data['address2']
    address.City = data['city']
    address.State = data['state']
    address.Zip5 = data['zipcode']
    return address

  def get_rate(self, city, state, postal_code):
    address = self.client.factory.create('Address')
    address.Address1 = ""
    address.Address2 = ""
    address.City = city
    address.State = state
    address.Zip5 = postal_code

    cart_items = self.client.factory.create('ArrayOfCartItem')
    cart_item = self.client.factory.create('CartItem')
    cart_item.Index = 1
    cart_item.ItemID = 1
    cart_item.TIC = 0
    cart_item.Price = Decimal("1.00")
    cart_item.Qty = 1
    cart_items.CartItem = [cart_item]

    response = self.client.service.Lookup(self.api_login_id, self.api_key, "NoCustomerID", "NoCartID",
                                        cart_items, address, address, True, 'false')

    if( response.ResponseType == 'Error' ):
      raise TaxCloudException(response.Messages[0][0].Message)

    return Decimal(str(response.CartItemsResponse[0][0].TaxAmount))
