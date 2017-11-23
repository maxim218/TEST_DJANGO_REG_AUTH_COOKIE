from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^my_page_with_form/', views.my_page_with_form, name='my_page_with_form'),
    url(r'^my_page_with_answer/', views.my_page_with_answer, name='my_page_with_answer'),
    url(r'^count_summa_of_numbers/', views.count_summa_of_numbers, name='count_summa_of_numbers'),

    url(r'^my_cookie_set/', views.my_cookie_set, name='my_cookie_set'),
    url(r'^my_cookie_delete/', views.my_cookie_delete, name='my_cookie_delete'),
    url(r'^my_cookie_get/', views.my_cookie_get, name='my_cookie_get'),


    url(r'^reg_my_user/', views.reg_my_user, name='reg_my_user'),
    url(r'^go_to_account/', views.go_to_account, name='go_to_account'),
    url(r'^is_i_am_authorized/', views.is_i_am_authorized, name='is_i_am_authorized'),
    url(r'^exit_from_my_account/', views.exit_from_my_account, name='exit_from_my_account'),
]
