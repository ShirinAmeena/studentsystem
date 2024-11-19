from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Course,Session_Year,CustomUser,Student,Staff,Subject,Staff_Notifications,Staff_leave,Staff_Feedback,Student_Notifications,Student_Feedback
from django.contrib import messages

@login_required(login_url='dologin')
def Student_views(request):
    return render(request,'Student/home.html')

@login_required(login_url='dologin')
def student_notifications(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notifications.objects.filter(student_id=student_id)

        context = {
            'notification': notification,
        }
    return render(request,'Student/notifications.html',context)

@login_required(login_url='dologin')
def student_notifications_done(request,status):
    notification = Student_Notifications.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('student_notifications')

@login_required(login_url='dologin')
def student_feedback(request):
    student_id = Student.objects.get(admin=request.user.id)
    feedback_history = Student_Feedback.objects.filter(student_id=student_id)
    context ={
        'feedback_history':feedback_history,
    }
    return render(request,'Student/feedback.html',context)


@login_required(login_url='dologin')
def student_save_feedback(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        student = Student.objects.get(admin=request.user.id)
        feedback = Student_Feedback(
            student_id=student,
            feedback=feedback,
            feedback_reply='',
        )
        feedback.save()
        messages.success(request, 'Feedback Sent Successfully')
        return redirect('student_save_feedback')
    return render(request, 'Student/feedback.html')
