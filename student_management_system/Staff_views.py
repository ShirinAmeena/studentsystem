from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Staff,Staff_Notifications,Staff_leave,Staff_Feedback
from django.contrib import messages
@login_required(login_url='dologin')
def Staff_views(request):
    return render(request,'Staff/home.html')
@login_required(login_url='dologin')

def notifications(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        notification = Staff_Notifications.objects.filter(staff_id = staff_id)

        context = {
            'notification':notification,
        }
    return render(request,'Staff/notifications.html',context)
@login_required(login_url='dologin')
def notifications_done(request,status):
    notification = Staff_Notifications.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('notifications')
@login_required(login_url='dologin')
def apply_leave(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        staff_leave_history = Staff_leave.objects.filter(staff_id=staff_id)
        context = {
            'staff_leave_history': staff_leave_history,
        }
    return render(request, 'Staff/apply_leave.html', context)

@login_required(login_url='dologin')
def add_apply_leave(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        staff = Staff.objects.get(admin=request.user.id)
        leave = Staff_leave(
            staff_id = staff,
            data = leave_date,
            message = leave_message,
        )
        leave.save()
        messages.success(request,'Leave Successfully Sent')
        return redirect('apply_leave')

@login_required(login_url='dologin')
def staff_feedback(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)
    context ={
        'feedback_history':feedback_history,
    }
    return render(request,'Staff/feedback.html',context)

@login_required(login_url='dologin')
def save_feedback(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        staff = Staff.objects.get(admin = request.user.id)
        feedback = Staff_Feedback(
            staff_id = staff,
            feedback = feedback,
            feedback_reply = '',
        )
        feedback.save()
        messages.success(request,'Feedback Sent Successfully')
        return redirect('staff_feedback')
    return render(request, 'Staff/feedback.html')


