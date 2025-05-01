from django.http import HttpResponse
from .function import fetch_students_data  

def get_students(request):
    students = fetch_students_data()
    content = ""
    for i, student in enumerate(students, start=1):
        content += f"<h3>student {i}:</h3>"
        content += f"<p>name: {student['name']}</p>"
        content += f"<p>age: {student['age']}</p>"
        content += f"<p>major: {student['major']}</p><hr>"

    return HttpResponse(content)