from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Bloodgroup, DonorReg, BloodRequest, Contact

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('user_type', 'profile_pic')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('user_type', 'profile_pic')}),
    )

class BloodgroupAdmin(admin.ModelAdmin):
    list_display = ('bloodgroup', 'created_at', 'updated_at')

class DonorRegAdmin(admin.ModelAdmin):
    list_display = ('admin', 'age', 'mobilenumber', 'bloodgroup', 'gender', 'address', 'status', 'regdate_at', 'updated_at')

class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('donid', 'fullname', 'mobno', 'email', 'requirer', 'message', 'regdate_at', 'updated_at')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'mobno', 'email', 'message', 'status', 'regdate_at', 'updated_at')

# Registering models to admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Bloodgroup, BloodgroupAdmin)
admin.site.register(DonorReg, DonorRegAdmin)
admin.site.register(BloodRequest, BloodRequestAdmin)
admin.site.register(Contact, ContactAdmin)
