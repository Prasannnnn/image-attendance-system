from django.shortcuts import render, redirect
from .forms import PersonForm

def capture_image(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PersonForm()
    return render(request, 'capture_image.html', {'form': form})

def success(request):
    return render(request, 'success.html')


from django.shortcuts import render
from .models import Person

def list_persons(request):
    persons = Person.objects.all()
    return render(request, 'list_persons.html', {'persons': persons})


import cv2
from django.http import JsonResponse
from django.utils import timezone
from .models import Person

def capture_image_auto(request):
    # Capture the image using OpenCV
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        # Save the captured image
        image_name = f"attendance_{timezone.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        image_path = f'media/images/{image_name}'
        cv2.imwrite(image_path, frame)

        # Here, implement your face recognition logic to identify the student
        # For simplicity, let's assume you have a function identify_student that returns the student's ID
        student_id = identify_student(frame)

        if student_id:
            # Record the attendance
            person = Person.objects.get(id_number=student_id)
            # You can also add an Attendance model to keep track of attendance records separately
            attendance_time = timezone.now()
            # Save the attendance record (this could be a new model)
            # For example: Attendance.objects.create(person=person, timestamp=attendance_time)
            return JsonResponse({'status': 'success', 'student_id': student_id, 'time': attendance_time})

    return JsonResponse({'status': 'failure'})

def identify_student(image):
    # Placeholder function for face recognition logic
    # This function should return the student's ID if recognized, otherwise None
    return "student_id_example"
