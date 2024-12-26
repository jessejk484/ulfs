import requests
import datetime

def get_token():
    url = "https://login.microsoftonline.com/1572400a-cb81-42c6-9433-55f87848d31b/oauth2/token"
    payload = 'grant_type=client_credentials&client_id=343c9dcb-de5e-4753-ad02-bf736bd18f3a&client_secret=sfd8Q~MkemZVQqyncbcN1egrLfr3dOlz1MRdvc5U&resource=https%3A%2F%2Fmanagement.azure.com%2F'


    response = requests.request("POST", url, data=payload)

    return response.json()['access_token']

def get_requests_data(token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f'https://management.azure.com/subscriptions/176469b5-f8a1-4b15-aaef-97797722e259/resourcegroups/info5900/providers/Microsoft.Web/sites/ulfs/providers/microsoft.Insights/metrics?timespan={from_date}/{to_date}&interval=PT1M&metricnames=Requests&aggregation=total&autoadjusttimegrain=true&validatedimensions=false&api-version=2019-07-01'
    r = requests.get(url, headers=headers)
    return r.json()['value'][0]['timeseries'][0]['data']


def get_response_times(token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f"https://management.azure.com/subscriptions/176469b5-f8a1-4b15-aaef-97797722e259/resourcegroups/info5900/providers/Microsoft.Web/sites/ulfs/providers/microsoft.Insights/metrics?timespan={from_date}/{to_date}&interval=PT1M&metricnames=HttpResponseTime&aggregation=average&autoadjusttimegrain=true&validatedimensions=false&api-version=2019-07-01"
    r = requests.get(url, headers=headers)
    return r.json()['value'][0]['timeseries'][0]['data']

def get_500_errors(token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f'https://management.azure.com/subscriptions/176469b5-f8a1-4b15-aaef-97797722e259/resourcegroups/info5900/providers/Microsoft.Web/sites/ulfs/providers/microsoft.Insights/metrics?timespan={from_date}/{to_date}&interval=PT1M&metricnames=Http5xx&aggregation=total&autoadjusttimegrain=true&validatedimensions=false&api-version=2019-07-01'
    r = requests.get(url, headers=headers)
    return r.json()['value'][0]['timeseries'][0]['data']

def get_500_agg(token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f'https://management.azure.com//subscriptions/176469b5-f8a1-4b15-aaef-97797722e259/resourceGroups/info5900/providers/Microsoft.Web/sites/ulfs/providers/microsoft.Insights/metrics?timespan={from_date}/{to_date}&interval=FULL&metricnames=Http5xx&aggregation=total&validatedimensions=false&api-version=2019-07-01'
    r = requests.get(url, headers=headers)
    return r.json()['value'][0]['timeseries'][0]['data'][0].get('total', '0')

def get_data_in(token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f'https://management.azure.com/subscriptions/176469b5-f8a1-4b15-aaef-97797722e259/resourceGroups/info5900/providers/Microsoft.Web/sites/ulfs/providers/microsoft.Insights/metrics?timespan={from_date}/{to_date}&interval=PT1M&metricnames=BytesReceived&aggregation=total&autoadjusttimegrain=true&validatedimensions=false&api-version=2019-07-01'
    r = requests.get(url, headers=headers)
    return r.json()['value'][0]['timeseries'][0]['data']

def get_data_in_agg(token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f'https://management.azure.com/subscriptions/176469b5-f8a1-4b15-aaef-97797722e259/resourceGroups/info5900/providers/Microsoft.Web/sites/ulfs/providers/microsoft.Insights/metrics?timespan={from_date}/{to_date}&interval=FULL&metricnames=BytesReceived&aggregation=total&validatedimensions=false&api-version=2019-07-01'
    r = requests.get(url, headers=headers)
    print(r.json())
    return r.json()['value'][0]['timeseries'][0]['data'][0].get('total', 0)

def get_data_out(token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f'https://management.azure.com/subscriptions/176469b5-f8a1-4b15-aaef-97797722e259/resourceGroups/info5900/providers/Microsoft.Web/sites/ulfs/providers/microsoft.Insights/metrics?timespan={from_date}/{to_date}&interval=PT1M&metricnames=BytesSent&aggregation=total&autoadjusttimegrain=true&validatedimensions=false&api-version=2019-07-01'
    r = requests.get(url, headers=headers)
    return r.json()['value'][0]['timeseries'][0]['data']

def get_data_out_agg(token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f'https://management.azure.com/subscriptions/176469b5-f8a1-4b15-aaef-97797722e259/resourceGroups/info5900/providers/Microsoft.Web/sites/ulfs/providers/microsoft.Insights/metrics?timespan={from_date}/{to_date}&interval=FULL&metricnames=BytesSent&aggregation=total&validatedimensions=false&api-version=2019-07-01'
    r = requests.get(url, headers=headers)
    return r.json()['value'][0]['timeseries'][0]['data'][0].get('total', 0)

def get_requests_agg(token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f'https://management.azure.com/subscriptions/176469b5-f8a1-4b15-aaef-97797722e259/resourceGroups/info5900/providers/Microsoft.Web/sites/ulfs/providers/microsoft.Insights/metrics?timespan={from_date}/{to_date}&interval=FULL&metricnames=Requests&aggregation=total&validatedimensions=false&api-version=2019-07-01'
    r = requests.get(url, headers=headers)
    return r.json()['value'][0]['timeseries'][0]['data'][0].get('total', 0)

def get_response_agg(token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f'https://management.azure.com/subscriptions/176469b5-f8a1-4b15-aaef-97797722e259/resourceGroups/info5900/providers/Microsoft.Web/sites/ulfs/providers/microsoft.Insights/metrics?timespan={from_date}/{to_date}&interval=FULL&metricnames=HttpResponseTime&aggregation=average&validatedimensions=false&api-version=2019-07-01'
    r = requests.get(url, headers=headers)
    return r.json()['value'][0]['timeseries'][0]['data'][0].get('average', 0)

def sa_data():
    token = get_token()
    utc_now = datetime.datetime.utcnow()
    to_date = utc_now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    one_hour_ago = utc_now - datetime.timedelta(hours=1)
    from_date = one_hour_ago.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

    requests_timeseries = get_requests_data(token, from_date, to_date)
    response_timeseries = get_response_times(token, from_date, to_date)
    errors_500 = get_500_errors(token, from_date, to_date)
    data_in = get_data_in(token, from_date, to_date)
    data_out = get_data_out(token, from_date, to_date)
    errors_500_agg = get_500_agg(token, from_date, to_date)
    data_in_agg = get_data_in_agg(token, from_date, to_date)/1024
    data_out_agg = get_data_out_agg(token, from_date, to_date)/1024
    requests_agg = get_requests_agg(token, from_date, to_date)
    response_agg = get_response_agg(token, from_date, to_date)*1000
    return (requests_timeseries, response_timeseries, errors_500, data_in, data_out, requests_agg, response_agg, errors_500_agg, data_in_agg, data_out_agg)
