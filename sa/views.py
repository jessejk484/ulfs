from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import sa_data

# Create your views here.
@login_required
def homePage(request):
    if str(request.user) != 'sa':
        messages.error(request, 'Restriced Route')
        return redirect('home')
    requests_timeseries, response_timeseries, errors_500, data_in, data_out, requests_agg, response_agg, errors_500_agg, data_in_agg, data_out_agg = sa_data()

    r_e5_x = []
    r_e5_y = []
    for i in errors_500:
        r_e5_x.append(str(i.get('timeStamp', None)))
        r_e5_y.append(i.get('total', 0))

    d_i_x = []
    d_i_y = []
    for i in data_in:
        d_i_x.append(str(i.get('timeStamp', None)))
        d_i_y.append(round(i.get('total', 0)/1000,2))

    d_o_x = []
    d_o_y = []
    for i in data_out:
        d_o_x.append(str(i.get('timeStamp', None)))
        d_o_y.append(round(i.get('total', 0)/1000,2))

    r_x = []
    r_y = []
    for i in requests_timeseries:
        r_x.append(str(i.get('timeStamp', None)))
        r_y.append(i.get('total', 0))

    rs_x = []
    rs_y = []
    for i in response_timeseries:
        rs_x.append(str(i.get('timeStamp', None)))
        rs_y.append(i.get('average', 0)*1000)

    context = {
        'title': 'System Admin Dashboard',
        'r_e5_y': str(r_e5_y),
        'r_e5_x': r_e5_x,
        'e5_agg': errors_500_agg,
        'data_in_agg': round(data_in_agg,2),
        'd_i_y': str(d_i_y),
        'd_i_x': d_i_x,
        'data_out_agg': round(data_out_agg,2),
        'd_o_y': str(d_o_y),
        'd_o_x': d_o_x,
        'r_agg': requests_agg,
        'r_x': r_x,
        'r_y': r_y,
        'rs_x': rs_x,
        'rs_y': rs_y,
        'rs_agg': round(response_agg, 2)
    }
    return render(request, 'sa/home.html', context)