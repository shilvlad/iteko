# Generated by Django 2.2.5 on 2019-10-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0003_helpdeskincidents_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpdeskincidents',
            name='state',
            field=models.CharField(choices=[('new', 'Новый'), ('worked', 'В работе'), ('wait', 'В ожидании'), ('done', 'Выполнена'), ('closed', 'Закрыта'), ('rework', 'Доработка')], default='new', editable=False, max_length=100),
        ),
    ]
