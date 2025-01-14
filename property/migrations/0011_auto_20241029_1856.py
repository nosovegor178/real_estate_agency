from django.db import migrations, models, transaction
import phonenumbers
from phonenumber_field.modelfields import PhoneNumberField


def fill_correct_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flat_objects = Flat.objects.all()
    for flat_object in flat_objects.iterator():
        parsed_number = phonenumbers.parse(flat_object.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parsed_number):
            pure_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
            flat_object.pure_phone = pure_number
            flat_object.save(update_fields=['pure_phone'])
        

def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all().update(owner_pure_phone = None)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20241029_1849'),
    ]



    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=PhoneNumberField(region=None, null=True, verbose_name='Нормализованный номер владельца'),
        ),

        migrations.RunPython(fill_correct_phonenumber, move_backward)
    ]
