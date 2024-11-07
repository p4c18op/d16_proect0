
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresponse',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userresponses', to='app.post'),
        ),
    ]
