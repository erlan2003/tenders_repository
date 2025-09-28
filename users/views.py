from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q

def open_users(request):
    users = User.objects.all()
    query = request.GET.get('q')
    if query:
        users = users.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(username__icontains=query)
        )
    sort = request.GET.get('sort')
    allowed_sort_fields = ['id', '-id', 'first_name', '-first_name',
                           'last_name', '-last_name', 'username', '-username',
                           'email', '-email', 'date_joined', '-date_joined']
    if sort in allowed_sort_fields:
        users = users.order_by(sort)

    return render(request, 'users.html', {'users': users})