from django.contrib import admin
from .models import administrator_login,administrator_signin, administrator_questions

# Register your models here.
class administratorAdmin(admin.ModelAdmin):
    list_display= ('firstname', 'lastname', 'admin_id', 'image', 'email_id', 'password')
    list_editable= ('lastname', 'admin_id')


admin.site.register(administrator_login, administratorAdmin)

class administrator_signinAdmin(admin.ModelAdmin):
    list_display= ['email_id', 'password']
    # list_editable= ('admin_id', 'email_id')


admin.site.register(administrator_signin, administrator_signinAdmin)

class administrator_questionsAdmin(admin.ModelAdmin):
    list_display= ['question', 'option_A', 'option_B', 'option_C', 'option_D']
    # list_editable= ('question', 'option_A', 'option_B', 'option_C', 'option_D')


admin.site.register(administrator_questions, administrator_questionsAdmin)





