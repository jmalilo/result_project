from django.urls import path
from result_app import views


urlpatterns=[
    path('',views.home,name='home'),
    path('result/<pk>',views.res_detail,name='res_detail'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_user,name='logout'),
    path('login/',views.login_user,name='login'),
    path('add_result/',views.result,name='add_result'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('admin_result/',views.admin_result,name='admin_result'),
    path('edit_result/<pk>',views.editresult,name='edit_result'),
    path('delete_result/<pk>',views.delete_result,name='delete_result'),
    path('parent_list',views.parent_list,name='parent_list'),
    path('edit_parent/<pk>',views.edit_parent,name='edit_parent'),
    path('delete_parent/<pk>',views.delete_parent,name='delete_parent'),
    path('parent_detail/<pk>',views.parent_detail,name='parent_detail'),
    path('download_pdf/<pk>',views.download_pdf,name='download_pdf'),
    path('add_fee',views.add_fee,name='add_fee'),
    path('fee_list',views.fee_list,name='fee_list'),
    path('edit_fee/<pk>',views.edit_fee,name='edit_fee'),
    path('fee_detail/<pk>',views.FeeDetail.as_view(),name='fee_detail'),
    path('student_list/',views.Student_list.as_view(),name='student_list'),
    path('student_detail/<pk>',views.Student_detail.as_view(),name='student_detail'),

]