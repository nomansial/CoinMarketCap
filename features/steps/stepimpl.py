from behave import *
import requests
import json
from assertpy import assert_that


from utilities.configurations import *

config = getConfig()


@given(u'API KEY is provided')
def step_impl(context):
    context.url = config['API']['retrieve']
    context.conversionURL = config['API']['conversion']
    context.infoURL = config['API']['info']
    context.headers = {'Accept': 'application/json', 'X-CMC_PRO_API_KEY': '7690a11a-cf25-4edb-850a-d534bd0104a3'}


@when(u'cryptocurrency map API is executed')
def step_impl(context):
    context.API_Response = requests.get(context.url, headers=context.headers)


@then(u'BTC USDT and ETH ID are retrieved')
def step_impl(context):
    json_object = context.API_Response.json()
    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)


@when(u'User provides {amount} and {currencyID} to covert to {secondCurrency}')
def step_impl(context, amount, currencyID, secondCurrency):
    context.Conversion_API_Response = requests.get(context.conversionURL, headers=context.headers,
                                                   params={'amount': amount, 'id': currencyID,
                                                           'convert': secondCurrency})


@then(u'Currency is converted successfully')
def step_impl(context):
    json_object_conversion = context.Conversion_API_Response.json()
    json_formatted_Conversion = json.dumps(json_object_conversion, indent=2)
    print(json_formatted_Conversion)


@when(u'cryptocurrency info API {ID} is provided')
def step_impl(context, ID):
    context.infoAPIresponse = requests.get(context.infoURL, headers=context.headers, params={'id': ID})


@then(u'response is received')
def step_impl(context):
    json_object_conversion = context.infoAPIresponse.json()
    json_formatted_Conversion = json.dumps(json_object_conversion, indent=2)
    print(json_formatted_Conversion)

    assert_that(json_object_conversion.get('data').get('1027').get('logo')).is_equal_to('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png')
    assert_that(json_object_conversion.get('data').get('1027').get('urls').get('technical_doc')).contains('ethereum/wiki/wiki/White-Paper')
    assert_that(json_object_conversion.get('data').get('1027').get('date_added')).contains('2015-08-07T00:00:00.000Z')
