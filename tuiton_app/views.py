from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"login.html")

def adm_add_batch(request):
    return render(request,"ADMIN/add batch management.html")
def adm_add_class(request):
    return render(request,"ADMIN/ADD CLASS MANAGEMENT.html")
def adm_add_fee_structure(request):
    return render(request,"ADMIN/add fee structure.html")
def adm_add_monthly_fee(request):
    return render(request,"ADMIN/add monthly fee.html")
def adm_add_monthly_fees(request):
    return render(request,"ADMIN/add monthy fees.html")

def adm_add_student(request):
    return render(request,"ADMIN/add student management.html")
def adm_add_subject(request):
    return render(request,"ADMIN/add subject management.html")
def adm_add_timetable(request):
    return render(request,"ADMIN/add timetable.html")
def adm_add_tutor(request):
    return render(request,"ADMIN/add tutor management.html")
def adm_add_tutors_subject(request):
    return render(request,"ADMIN/add tutor subject.html")
def adm_add_tutors_salary(request):
    return render(request,"ADMIN/Add tutors salary.html")
def adm_add_vacancy(request):
    return render(request,"ADMIN/Add vacancy.html")
def adm_due_report(request):
    return render(request,"ADMIN/due report.html")
def adm_give_reply(request):
    return render(request,"ADMIN/give reply.html")
def adm_update_batch(request):
    return render(request,"ADMIN/update batch management.html")
def adm_update_class(request):
    return render(request,"ADMIN/UPDATE CLASS MANAGEMENT.html")
def adm_update_fee_structure(request):
    return render(request,"ADMIN/update fee structure.html")
def adm_update_student(request):
    return render(request,"ADMIN/update student management.html")
def adm_update_subject(request):
    return render(request,"ADMIN/UPDATE SUBJECT MANAGEMENT.html")
def adm_update_timetable(request):
    return render(request,"ADMIN/ update timetable.html")
def adm_update_tutor(request):
    return render(request,"ADMIN/update tutor management.html")
def adm_update_tutors_subject(request):
    return render(request,"ADMIN/update tutor subject.html")
def adm_update_vacancy(request):
    return render(request,"ADMIN/update vacancy.html")
def adm_view_attendence_of_tutors(request):
    return render(request,"ADMIN/view attendence of tutors.html")
def adm_view_batch(request):
    return render(request,"ADMIN/view batch management.html")
def adm_view_class(request):
    return render(request,"ADMIN/View class management.html")
def adm_view_complaint(request):
    return render(request,"ADMIN/View complaint and give reply.html")
def adm_view_fee_structure(request):
    return render(request,"ADMIN/view fee structure.html")
def adm_view_feedback(request):
    return render(request,"ADMIN/view feedback.html")
def adm_view_leave_request(request):
    return render(request,"ADMIN/View leave request.html")
def adm_view_monthly_fee_reports(request):
    return render(request,"ADMIN/view monthly fee reports.html")
def adm_view_monthly_salary_reports(request):
    return render(request,"ADMIN/view monthly salary report.html")
def adm_view_student(request):
    return render(request,"ADMIN/view student management.html")
def adm_view_subject(request):
    return render(request,"ADMIN/VIEW SUBJECT MANAGEMENT.html")
def adm_view_timetable(request):
    return render(request,"ADMIN/view timetable.html")
def adm_view_tutor(request):
    return render(request,"ADMIN/view tutor management.html")
def adm_view_tutors_subject(request):
    return render(request,"ADMIN/view tutor subject.html")
def adm_view_vacancy(request):
    return render(request,"ADMIN/view vaccancy.html")
def adm_view_yearly_salary_reports(request):
    return render(request,"ADMIN/view yearly salary reports.html")



