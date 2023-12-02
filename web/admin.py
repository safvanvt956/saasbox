from django.contrib import admin
from . models import Email,Contact,Update,About,Gallery_image,Award,Busines,index_portfolio_form


# Register your models here.

admin.site.register(About)

admin.site.register(Gallery_image)

admin.site.register(Email)

admin.site.register(Busines)

# admin.site.register(Update)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullname','email','topics','message')


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('image','title','parashap','created_at')


@admin.register(Award)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('icon','title','parashpa')


@admin.register(index_portfolio_form)
class index_portfolio_formAdmin(admin.ModelAdmin):
    list_display = ('yourname','email','topics','message')












    

    

    

