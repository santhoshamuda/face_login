





# accounts/views.py
# views.py
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
import face_recognition
import base64
import numpy as np

CustomUser = get_user_model()

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        face_data_url = request.POST['face_data']

        # Username already exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        try:
            face_data = base64.b64decode(face_data_url.split(',')[1])
            with open('temp.jpg', 'wb') as f:
                f.write(face_data)

            image = face_recognition.load_image_file('temp.jpg')
            face_encodings = face_recognition.face_encodings(image)

            if face_encodings:
                user = CustomUser(username=username)
                user.set_password(password)
                user.face_encoding = face_encodings[0].tobytes()
                user.save()
                messages.success(request, "Registered successfully! Please log in.")
                return redirect('login')
            else:
                messages.error(request, "No face detected. Please try again.")
                return redirect('register')

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('register')

    return render(request, 'accounts/register.html')  # ✅ use separate register page

# def user_login(request):
def user_login(request):
    if request.method == 'POST':
        face_data_url = request.POST.get('face_data')

        try:
            face_data = base64.b64decode(face_data_url.split(',')[1])
            with open('temp_login.jpg', 'wb') as f:
                f.write(face_data)

            image = face_recognition.load_image_file('temp_login.jpg')
            face_encodings = face_recognition.face_encodings(image)

            if face_encodings:
                login_face_encoding = face_encodings[0]

                for user in CustomUser.objects.all():
                    known_encoding = np.frombuffer(user.face_encoding)

                    match = face_recognition.compare_faces(
                        [known_encoding],
                        login_face_encoding,
                        tolerance=0.5
                    )[0]

                    if match:
                        # ✅ Properly fetch and login the matched user
                        matched_user = CustomUser.objects.get(id=user.id)
                        login(request, matched_user)
                        messages.success(request, f"Welcome, {matched_user.username}!")
                        return redirect('dashboard')

                messages.error(request, "Face not recognized. Try again.")
                return redirect('login')

            else:
                messages.error(request, "No face detected.")
                return redirect('login')

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('login')

    return render(request, 'accounts/login.html')

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'user': request.user})

def user_logout(request):
    logout(request)
    
    request.session.flush()
    messages.success(request, "Logged out successfully!")
    return redirect('home')
    
    

############################################



###################################################

