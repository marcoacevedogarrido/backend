# Generated by Django 4.1.3 on 2022-12-12 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0002_perfil_remove_jefatura_usuariojefatura_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentos_institucionales', models.CharField(blank=True, max_length=50, null=True)),
                ('finanzas', models.CharField(blank=True, max_length=50, null=True)),
                ('servicios_bancarios', models.CharField(blank=True, max_length=50, null=True)),
                ('rrhh', models.CharField(blank=True, max_length=50, null=True)),
                ('directorio_de_contactos', models.CharField(blank=True, max_length=50, null=True)),
                ('productos_institucionales', models.CharField(blank=True, max_length=50, null=True)),
                ('correo_electrónico', models.EmailField(blank=True, max_length=50, null=True)),
                ('bases_de_datos_internos', models.CharField(blank=True, max_length=50, null=True)),
                ('bases_de_datos_externos', models.CharField(blank=True, max_length=50, null=True)),
                ('bases_de_datos_colaborativos', models.CharField(blank=True, max_length=50, null=True)),
                ('pagina_web_interna', models.CharField(blank=True, max_length=50, null=True)),
                ('pagina_web_externa', models.CharField(blank=True, max_length=50, null=True)),
                ('respaldos', models.CharField(blank=True, max_length=50, null=True)),
                ('infraestructura', models.CharField(blank=True, max_length=50, null=True)),
                ('informatica', models.CharField(blank=True, max_length=50, null=True)),
                ('base_de_datos_de_contrasenas', models.CharField(blank=True, max_length=50, null=True)),
                ('datos_e_informacion_no_institucionales', models.CharField(blank=True, max_length=50, null=True)),
                ('navegacion_en_internet', models.CharField(blank=True, max_length=50, null=True)),
                ('chat_interno', models.CharField(blank=True, max_length=50, null=True)),
                ('chat_externo', models.CharField(blank=True, max_length=50, null=True)),
                ('llamadas_telefonicas_internas', models.CharField(blank=True, max_length=50, null=True)),
                ('llamadas_telefonicas_externas', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]