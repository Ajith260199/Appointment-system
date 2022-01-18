from django.shortcuts import render
from django.contrib import messages
from .models import user_details_table
import secrets, string
from datetime import date

today_date = date.today()
working_hours = (['09:00', '09:30', '10:00', '10:30', '11:00',
                  '11:30', '12:00', '12:30', '13:00', '14:30',
                  '15:00', '15:30', '16:00', '16:30', '17:00', '17:30'])


def ap_booking(request):
    try:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            number = request.POST['contactnumber']
            date_time = request.POST['datetime']
            print(date_time)
            if date_time[11:16] in working_hours and date_time[:10] >= str(today_date):
                alphabet_for_patient_id = string.ascii_letters + string.digits
                patient_id = ''.join(secrets.choice(alphabet_for_patient_id) for i in range(10))
                user_details = user_details_table(name=name, email=email, number=number, date_time=date_time,
                                                  patient_id=patient_id)
                user_details.save()
                messages.success(request, 'hi ' + name + ' appointment made successfully and your patient id is '
                                  + patient_id + ' save this for future reference')
                return render(request, "base.html")
            else:
                messages.error(request, 'A date should not be earlier than date and'
                                        'time should be like 00.00 hours or 00.30 hours')
    except:
        messages.error(request, 'incorrect contact number or appointment not available on the date you called')
    finally:
        return render(request, "base.html")


def ap_cancel(request):
    try:
        if request.method == 'POST':
            form_patient_id = request.POST['patient_id']
            db_patient_id = user_details_table.objects.get(patient_id=form_patient_id)
            user_details_table.objects.filter(pk=db_patient_id.pk).delete()
            messages.success(request, 'appointment successfully cancelled')
            return render(request, "base.html")
        else:
            return render(request,"cancel.html")
    except:
        messages.error(request, 'no records found based on your patient id')
        return render(request, "cancel.html")


def ap_reschedule(request):
    try:
        if request.method == "POST":
            form_patient_id = request.POST['patient_id']
            form_datetime  = request.POST['datetime']
            if form_datetime[11:16] in working_hours and form_datetime[:10] >= str(today_date):
                db_patient_id = user_details_table.objects.get(patient_id=form_patient_id)
                user_details_table.objects.filter(pk=db_patient_id.pk).update(date_time = form_datetime)
                messages.success(request, 'appointment rescheduled successfully')
                return render(request, 'base.html')
            else:
                messages.error(request, 'A date should not be earlier than date and'
                                        'time should be like 00.00 hours or 00.30 hours')
                return render(request,'reschedule.html')
        else:
            return render(request,'reschedule.html')
    except:
        messages.error(request, 'no records found based on your patient id')
        return render(request, "reschedule.html")