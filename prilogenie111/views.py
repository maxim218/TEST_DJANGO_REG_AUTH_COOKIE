from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def my_page_with_form(request):
    return render(request, 'prilogenie111/my_page_with_form.html', {})

def my_page_with_answer(request):
    return render(request, 'prilogenie111/my_page_with_answer.html', {})

def count_summa_of_numbers(request):
    a = str( request.POST['a'] )
    b = str( request.POST['b'] )
    summa = float(a) + float(b)

    print("Find Summa:")
    print(a)
    print(b)
    print(summa)

    return HttpResponseRedirect("/my_page_with_answer/" + str(summa))




def my_cookie_set(request):
    request.session["my_cookie_variable"] = str(request.GET['xxx'])
    return HttpResponse("Значение куки успешно задано")

def my_cookie_delete(request):
    if ("my_cookie_variable" in request.session) == False:
        return HttpResponse(str("Куки НЕ существует"))
    else:
        request.session.pop("my_cookie_variable")
        return HttpResponse(str("Куки успешно удалена"))


def my_cookie_get(request):
    if ("my_cookie_variable" in request.session) == False:
        return HttpResponse(str("Куки НЕ существует"))
    else:
        value = request.session["my_cookie_variable"]
        return HttpResponse("Значение куки: " + str(value))




from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def reg_my_user(request):
    # get params from post query
    user_login = str( request.POST['userLogin'] )
    user_password = str( request.POST['userPassword'] )

    # try to find user in db
    users = User.objects.filter(username=user_login)

    if len(users) > 0:
        # user is already exists in DB
        return HttpResponseRedirect("/my_page_with_form/" + "user_is_already_exists_in_db")
    else:
        # registrate new user
        user = User.objects.create_user(user_login, user_login + "@abc.ru", user_password)
        user.save()
        return HttpResponseRedirect("/my_page_with_form/" + "create_user_ok")


def go_to_account(request):
    # get params from post query
    user_login = str( request.POST['loginOfUser'] )
    user_password = str( request.POST['passwordOfUser'] )

    # try to get user in Db
    user = authenticate(username=user_login, password=user_password)

    # if user exists
    if user is not None:
        # authorize user
        login(request, user)
        return HttpResponseRedirect("/my_page_with_form/" + "authorize_ok")
    else:
        # not correct login or password
        return HttpResponseRedirect("/my_page_with_form/" + "not_correct_login_or_password")


def is_i_am_authorized(request):
    if request.user.is_authenticated():
        user_login = str(request.user.username)
        return HttpResponse("Вы авторизованы как " + user_login)
    else:
        return HttpResponse("Вы НЕ авторизованы")


def exit_from_my_account(request):
    if request.user.is_authenticated():
        logout(request)
    return HttpResponse("Вы вышли")
