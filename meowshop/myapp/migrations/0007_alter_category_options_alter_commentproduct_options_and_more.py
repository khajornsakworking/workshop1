# Generated by Django 4.0.5 on 2022-06-08 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_commentproduct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='commentproduct',
            options={'ordering': ['id'], 'verbose_name_plural': 'CommentProduct'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-p_created'], 'verbose_name_plural': 'Product'},
        ),
        migrations.AddField(
            model_name='product',
            name='p_image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
    ]
