from django.contrib import admin
from .models import StaffDetail, StudentDetail, ClassLecture, DisciplinaryIssue, CharacterCertificate, Course

admin.site.register(StaffDetail)
admin.site.register(StudentDetail)
admin.site.register(ClassLecture)
admin.site.register(Course)
admin.site.register(DisciplinaryIssue)
admin.site.register(CharacterCertificate)
