from django.contrib import admin
from .models import Cliente,Contacto,Maquina,Orden,Pedido,Pieza,Area,Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=("user","address","location","telephone","user_group")
    search_fields=("location","user","user__username","user__groups__name")
    list_filter=("user__groups","location")
    
    def user_group(self,obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])
    user_group.short_description='Grupo'
admin.site.register(Profile,ProfileAdmin)


class ClienteAdmin(admin.ModelAdmin):
    list_display=("id_cli","nom_cli","apell_cli","tel_cli","dir_cli","email_cli")
admin.site.register(Cliente,ClienteAdmin)

class ContactoAdmin(admin.ModelAdmin):
    list_display=("codigo","nombre","email_con","asunto","mensaje")
admin.site.register(Contacto,ContactoAdmin)

class MaquinaAdmin(admin.ModelAdmin):
    list_display=("cod_maquina","nom_maquina","tipo_maquina","cant_component","imagen")
admin.site.register(Maquina,MaquinaAdmin)

class OrdenAdmin(admin.ModelAdmin):
    list_display=("cod_ord","fecha_entrega","cod_maquina","cant","cod_area","remision_img","cod_ped")
admin.site.register(Orden,OrdenAdmin)

class PedidoAdmin(admin.ModelAdmin):
    list_display=("cod_ped","fecha_ped","cod_maquina","precio","cantidad","total","observaciones","id_cli")
admin.site.register(Pedido,PedidoAdmin)

class PiezaAdmin(admin.ModelAdmin):
    list_display=("cod_pieza","nom_pieza","tipo_material","stock","cod_maquina")
admin.site.register(Pieza,PiezaAdmin)

class AreaAdmin(admin.ModelAdmin):
    list_display=("cod_area","nombre","email_area")
admin.site.register(Area,AreaAdmin)
