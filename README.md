# Student API Project

مشروع Django بسيط يعرض بيانات 5 طلاب من خلال API.

# كيفية تشغيل السيرفر المحلي

### 1. إنشاء بيئة افتراضية وتفعيلها:
قبل البدء، تأكدت من أني في مجلد المشروع، ثم قمت بإنشاء بيئة افتراضية وتشغيلها
python -m venv env
env\Scripts\activate
### 2.ثم تعليمة لتشغيل سيرفر محلي على الجهاز
python manage.py runserver

# كيفية تجريب ال Api 
بعد تشغيل السيرفر، افتح المتصفح واذهب إلى العنوان التالي

http://127.0.0.1:8000/students/

وستظهر النتيجة بالشكل

student 1:

name: Aya
age: 22
major: Information Engineering
-------------------------------------
student 2:

name: Esraa
age: 23
major: Computer Engineering
-------------------------------------
student 3:

name: Enas
age: 21
major: Medical Engineering
-------------------------------------
student 4:

name: Malak
age: 22
major: Communications Engineering
-------------------------------------
student 5:

name: Elaf
age: 22
major: Information Engineering

