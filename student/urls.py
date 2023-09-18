from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('change_password/',auth_views.PasswordChangeView.as_view(template_name = 'student/pay_installment.html',success_url = reverse_lazy('home')),name='change_password'),

    path('',views.home,name='home'),
    path('student/',views.student_list,name='student_list'),
    path('add_student/',views.add_student,name='add_student'),
    path('update_student/<int:id>/',views.update_student,name='update_student'),
    path('delete_student/<int:id>/',views.delete_student,name='delete_student'),
    path('student_view/<int:id>/',views.student_view,name='student_view'),
    path('student_reports',views.student_reports,name='student_reports'),
    path('student_reports_excel',views.student_reports_excel,name='student_reports_excel'),


    path('student_list_with_fees/',views.student_list_with_fees,name='student_list_with_fees'),
    path('student_view_with_fees/<int:id>/',views.student_view_with_fees,name='student_view_with_fees'),
    path('student_view_with_fees/<int:id>/add_show_fees',views.add_show_fee,name='add_show_fee'),
    path('student_view_with_fees/<int:sid>/delete_show_fees/<int:id>',views.delete_show_fee,name='delete_show_fee'),
    path('student_fees_reports',views.Fees_Reports,name='Fees_Reports'),
    path('payment_fees_reports',views.Fees_Payment_Reports,name='Fees_Payment_Reports'),


    path('student_list_with_installment/',views.student_list_with_installment,name='student_list_with_installment'),
    path('student_view_with_installment/<int:id>/',views.student_view_with_installment,name='student_view_with_installment'),
    path('student_view_with_installment/<int:id>/pay_installment',views.pay_installment,name='pay_installment'),
    path('student_view_with_installment/<int:sid>/Edit_installment_fee/<int:id>',views.edit_installment_fee,name='edit_installment_fee'),
    path('student_view_with_installment/<int:sid>/delete_installment_fee/<int:id>',views.delete_installment_fee,name='delete_installment_fee'),


    path('courses',views.courses,name='courses'),
    path('courses_view/<int:id>',views.courses_view,name='courses_view'),
    path('courses_alter_view/',views.courses_alter_view,name='courses_alter_view'),
    path('add_courses/',views.courses_add,name='add_courses'),
    path('alter_courses/<int:id>',views.courses_alter,name='alter_courses'),
    path('delete_courses/<int:id>',views.courses_delete,name='delete_courses'),
    path('course_reports/',views.course_reports,name='course_reports'),


    path('enquries/',views.enquries,name='enquries'),
    path('enquries_alter_view/',views.enquries_alter_view,name='enquries_alter_view'),
    path('enquries_view/<int:id>',views.enquries_view,name='enquries_view'),
    path('add_enquries/',views.enquries_add,name='add_enquries'),
    path('delete_enquries/<int:id>',views.enquries_delete,name='delete_enquries'),
    path('enquries_reports/',views.enquries_reports,name='enquries_reports'),


    path('accounts/make_transactions',views.Make_Transaction,name='Make_Transaction'),
    path('accounts/view_transactions',views.View_Transaction,name='View_Transaction'),
    path('accounts/edit_transactions/<int:id>',views.Edit_Transaction,name='Edit_Transaction'),
    path('accounts/delete_transactions<int:id>',views.Delete_Transaction,name='Delete_Transaction'),
    path('accounts/transactions_reports',views.Transaction_Reports,name='Transaction_Reports'),
]