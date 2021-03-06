# Generated by Django 2.0.6 on 2018-07-31 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('comment_text', models.TextField()),
                ('comment_time', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rep_comment', to='blog.Comment')),
                ('rep_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rep_list', to=settings.AUTH_USER_MODEL)),
                ('top_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='top_level_comment', to='blog.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ['comment_time'],
            },
        ),
        migrations.AlterField(
            model_name='posts',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '草稿'), (1, '发布')], default=1),
        ),
    ]
