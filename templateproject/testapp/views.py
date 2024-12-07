from django.shortcuts import render
import datetime
import random


# please Create your views here.

def results1_view(request):
    get_date_time = datetime.datetime.now()
    my_dict = {'get_date_time': get_date_time}
    return render(request, 'testapp/results1.html', context=my_dict)


def results2_view(request):
    get_date_time = datetime.datetime.now()
    course = 'Django'
    prerequesite = 'Python'
    my_dict = {'get_date_time': get_date_time, 'course': course, 'prerequesite': prerequesite}
    return render(request, 'testapp/results2.html', context=my_dict)


def results3_view(request):
    msg_list = [
        'You will get marry soon',
        'You will get good job',
        'You will get good wife',
        'Tomorrow is the gud day to propose ur girl friend'
    ]
    names_list = [
        'Kareena Kapoor',
        'Deepika padukune',
        'Alia bhatt',
        'sunny'
    ]
    time = datetime.datetime.now()
    h = int(time.strftime('%H'))
    if h < 12:
        s = 'Gud Morning!'
    elif h < 16:
        s = 'Gud Afternoon!'
    elif h < 21:
        s = 'Gud Evening!'
    else:
        s = 'Gud Night!'
    msg = random.choice(msg_list)
    name = random.choice(names_list)
    my_dict = {'time': time, 'msg': msg, 'name': name, 'wish': s}
    return render(request, 'testapp/results3.html', context=my_dict)
