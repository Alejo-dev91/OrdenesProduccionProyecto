from django.db import models
from django.contrib.auth.models import User # Importar la tabla user que tiene Django por defecto
from django.db.models.signals import post_save


# Perfil de usuario
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',verbose_name='Usuario' )
    imagen=models.ImageField(default='users/usuario_defecto.jpg',upload_to='users/',verbose_name='Imagen de Perfil')
    address=models.CharField(max_length=150,null=True, blank=True,verbose_name='Direccion')
    location=models.CharField(max_length=150,null=True, blank=True,verbose_name='Ciudad')
    telephone=models.CharField(max_length=30,null=True, blank=True,verbose_name='Telefono')
    
    class Meta:
        verbose_name='perfil'
        verbose_name_plural='perfiles'
        ordering=['-id']
        
    def __str__(self):
        return self.user.username
    # Cuando se crea un usuario esta funcion crea automatico el perfil
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
    
post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)
    

    
    
class Area(models.Model):
    cod_area = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    email_area = models.CharField(max_length=45)
    
    def __str__(self):
        texto="{0}"
        return texto.format(self.nombre)

    


class Cliente(models.Model):
    id_cli = models.IntegerField(primary_key=True)
    nom_cli = models.CharField(max_length=45)
    apell_cli = models.CharField(max_length=45)
    tel_cli = models.CharField(max_length=45)
    dir_cli = models.CharField(max_length=45)
    email_cli = models.CharField(max_length=45)
    def __str__(self):
        texto="{0}"
        return texto.format(self.nom_cli,self.apell_cli)

    

opciones_consulta=[
    [0,"Consulta"],
    [1,"Reclamo"],
    [2,"Sugerencia"],
    [3,"Felicitación"]
]
class Contacto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    email_con = models.CharField(max_length=45)
    asunto = models.IntegerField(choices=opciones_consulta)
    mensaje = models.CharField(max_length=150)
    def __str__(self):
        texto="{0}"
        return texto.format(self.nombre)

    


class Maquina(models.Model):
    cod_maquina = models.IntegerField(primary_key=True)
    nom_maquina = models.CharField(max_length=45)
    tipo_maquina = models.CharField(max_length=45)
    cant_component = models.IntegerField()
    imagen = models.ImageField(upload_to='maquinas/', blank=True, null=True)

    
    def __str__(self):
        texto="{0}"
        return texto.format(self.nom_maquina)

    


class Orden(models.Model):
    cod_ord = models.IntegerField(primary_key=True)
    fecha_entrega = models.DateField()
    cod_maquina = models.ForeignKey(Maquina, models.DO_NOTHING, db_column='cod_maquina')
    cant = models.FloatField()
    cod_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='cod_area')
    remision_img = models.CharField(max_length=200)
    cod_ped = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='cod_ped')
    
    def __str__(self):
        texto="{0}"
        return texto.format(self.cod_ord)

    


class Pedido(models.Model):
    cod_ped = models.IntegerField(primary_key=True)
    fecha_ped = models.DateField()
    cod_maquina = models.ForeignKey(Maquina, models.DO_NOTHING, db_column='cod_maquina')
    precio = models.FloatField()
    cantidad = models.FloatField()
    total = models.FloatField()
    observaciones = models.CharField(max_length=45)
    id_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cli')
    
    def __str__(self):
        texto="{0}"
        return texto.format(self.cod_ped)

    


class Pieza(models.Model):
    cod_pieza = models.IntegerField(primary_key=True)
    nom_pieza = models.CharField(max_length=45)
    tipo_material = models.CharField(max_length=45)
    stock = models.IntegerField()
    cod_maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE, db_column='cod_maquina')
    
    def __str__(self):
        texto="{0}"
        return texto.format(self.nom_pieza)

    