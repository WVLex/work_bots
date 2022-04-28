# from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
#
# client_id = 'Aaszk8AlE1kES3PG3X3-TvR2ruZdOODzbYMa1uZyAFX_7fN1w4nvmgReQUm25RbcnkEFT2ZwsVenwKWa'
# secret = 'EMIud2vTJ1r-LYg-1N1eP4Yze-JXbWi0ldqJWRVYjeDzWbNUDsvGBavq8DwXPIYUJH3-pA1oT9aoyOS6'
#
#
# environment = SandboxEnvironment(client_id=client_id, client_secret=secret)
# client = PayPalHttpClient(environment)
#
# from paypalcheckoutsdk.orders import OrdersCreateRequest
# from paypalhttp import HttpError
# # Construct a request object and set desired parameters
# # Here, OrdersCreateRequest() creates a POST request to /v2/checkout/orders
# request = OrdersCreateRequest()
#
# request.prefer('return=representation')
#
# request.request_body (
#     {
#         "intent": "CAPTURE",
#         "purchase_units": [
#             {
#                 "amount": {
#                     "currency_code": "RUB",
#                     "value": "100.00"
#                 }
#             }
#         ]
#     }
# )
#
# try:
#     # Call API with your client and get a response for your call
#     response = client.execute(request)
#     print('Order With Complete Payload:')
#     print('Status Code:', response.status_code)
#     print('Status:', response.result.status)
#     print('Order ID:', response.result.id)
#     print('Intent:', response.result.intent)
#     print('Links:')
#     for link in response.result.links:
#         print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
#         print('Total Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
#         response.result.purchase_units[0].amount.value))
#         # If call returns body in response, you can get the deserialized version from the result attribute of the response
#         order = response.result
#         print(order)
# except IOError as ioe:
#     print(ioe)
#     if isinstance(ioe, HttpError):
#         # Something went wrong server-side
#         print(ioe.status_code)

import paypalrestsdk
import logging

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "Aaszk8AlE1kES3PG3X3-TvR2ruZdOODzbYMa1uZyAFX_7fN1w4nvmgReQUm25RbcnkEFT2ZwsVenwKWa",
  "client_secret": "ECcy5j_eya0kFK7aYnFqEGb6OWYQQ5Q43IFZ7ZEqFElFz_XvPgy6FNfaZLhtoxCnlU0dvwKXwMdsAIfd" })

payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},
    "transactions": [{
        "item_list": {
            "items": [{
                "name": "item",
                "sku": "item",
                "price": "5.00",
                "currency": "USD",
                "quantity": 1}]},
        "amount": {
            "total": "5.00",
            "currency": "USD"},
        "description": "This is the payment transaction description."}]})

if payment.create():
  print("Payment created successfully")
else:
  print(payment.error)


for link in payment.links:
    if link.rel == "approval_url":
        # Convert to str to avoid Google App Engine Unicode issue
        # https://github.com/paypal/rest-api-sdk-python/pull/58
        approval_url = str(link.href)
        print("Redirect for approval: %s" % (approval_url))