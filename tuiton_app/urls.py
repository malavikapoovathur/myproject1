from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login),
    path('adm_add_batch/', views.adm_add_batch),
    path('adm_add_class/', views.adm_add_class),
    path('adm_add_fee_structure/', views.adm_add_fee_structure),
    path('adm_add_monthly_fee/', views.adm_add_monthly_fee),
    path('adm_add_monthly_fees/', views.adm_add_monthly_fees),

    path('adm_add_student/', views.adm_add_student),
    path('adm_add_subject/', views.adm_add_subject),
    path('adm_add_timetable/', views.adm_add_timetable),
    path('adm_add_tutor/', views.adm_add_tutor),
    path('adm_add_tutors_subject/', views.adm_add_tutors_subject),
    path('adm_add_tutors_salary/', views.adm_add_tutors_salary),
    path('adm_add_vacancy/', views.adm_add_vacancy),
    path('adm_due_report/', views.adm_due_report),
    path('adm_give_reply/', views.adm_give_reply),
    path('adm_give_reply/', views.adm_update_batch),
    path('adm_update_class/', views.adm_update_class),
    path('adm_update_fee_structure/', views.adm_update_fee_structure),
    path('adm_update_student/', views.adm_update_student),
    path('adm_update_subject/', views.adm_update_subject),
    path('adm_update_timetable/', views.adm_update_timetable),
    path('adm_update_tutor/', views.adm_update_tutor),
    path('adm_update_tutors_subject/', views.adm_update_tutors_subject),
    path('adm_update_vacancy/', views.adm_update_vacancy),
    path('adm_view_attendence_of_tutors/', views.adm_view_attendence_of_tutors),
    path('adm_view_batch/', views.adm_view_batch),
    path('adm_view_class/', views.adm_view_class),
    path('adm_view_complaint/', views.adm_view_complaint),
    path('adm_view_fee_structure/', views.adm_view_fee_structure),
    path('adm_view_feedback/', views.adm_view_feedback),
    path('adm_view_leave_request/', views.adm_view_leave_request),
    path('adm_view_monthly_fee_reports/', views.adm_view_monthly_fee_reports),
    path('adm_view_monthly_salary_reports/', views.adm_view_monthly_salary_reports),
    path('adm_view_student/', views.adm_view_student),
    path('adm_view_subject/', views.adm_view_subject),
    path('adm_view_timetable/', views.adm_view_timetable),
    path('adm_view_tutor/', views.adm_view_tutor),
    path('adm_view_tutors_subject/', views.adm_view_tutors_subject),
    path('adm_view_vacancy/', views.adm_view_vacancy),
    path('adm_view_yearly_salary_reports)/', views.adm_view_yearly_salary_reports),




]
