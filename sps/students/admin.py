from django.contrib import admin
from.models import Students

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display= ('firstname', 'lastname', 'student_id', 'phy', 'chem', 'bio', 'maths', 'pcb', 'pcm')
    list_editable= ('phy','chem', 'bio', 'pcb', 'pcm')

admin.site.register(Students, StudentAdmin)

 