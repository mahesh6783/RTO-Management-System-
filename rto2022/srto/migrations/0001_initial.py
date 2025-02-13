# Generated by Django 3.2.4 on 2021-06-13 17:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Licenserate',
            fields=[
                ('lcode', models.IntegerField(primary_key=True, serialize=False, verbose_name='License  Code')),
                ('lname', models.CharField(max_length=100, verbose_name='License Name')),
                ('lfee', models.IntegerField(verbose_name='License Fee')),
                ('validity', models.IntegerField(verbose_name='Validity in Years')),
            ],
        ),
        migrations.CreateModel(
            name='Rtoffice',
            fields=[
                ('rcode', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='RT Office Code')),
                ('rname', models.CharField(max_length=100, verbose_name='RT Office Name')),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Taxrate',
            fields=[
                ('taxcode', models.IntegerField(primary_key=True, serialize=False, verbose_name='Tax Code')),
                ('vhtype', models.CharField(max_length=100, verbose_name='Type of Vehicle')),
                ('mop', models.CharField(max_length=100, verbose_name='Mode of Operation')),
                ('taxp', models.IntegerField(verbose_name='Tax Percentage')),
                ('duration', models.IntegerField(verbose_name='Validity in Years')),
            ],
        ),
        migrations.CreateModel(
            name='Useraccount',
            fields=[
                ('uname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('pword', models.CharField(max_length=100)),
                ('ids', models.CharField(max_length=100)),
                ('rights', models.CharField(max_length=15)),
                ('rcode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Leaners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adate', models.DateField(default=datetime.date.today, verbose_name='Application Date')),
                ('aname', models.CharField(max_length=50, verbose_name='Name of the Applicant')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('None', 'None')], default='Male', max_length=20, verbose_name='Gender')),
                ('fname', models.CharField(max_length=50, verbose_name="Father's Name")),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('adharno', models.CharField(max_length=20, verbose_name='Adhar No')),
                ('quali', models.CharField(max_length=50, verbose_name='Qualification')),
                ('lcode', models.IntegerField()),
                ('lname', models.CharField(max_length=50)),
                ('cardno', models.CharField(max_length=20, verbose_name='Credit Card No')),
                ('amtpaid', models.IntegerField()),
                ('testdate', models.DateField()),
                ('score', models.IntegerField(default=0)),
                ('lno', models.IntegerField(default=0)),
                ('vfrom', models.DateField()),
                ('vto', models.DateField()),
                ('status', models.CharField(default='N', max_length=50)),
                ('rcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srto.rtoffice')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('adharno', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Adhar No')),
                ('ename', models.CharField(max_length=100, verbose_name='Employee Name')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('None', 'None')], default='Male', max_length=20, verbose_name='Gender')),
                ('hname', models.CharField(max_length=100, verbose_name='House Name')),
                ('place', models.CharField(max_length=100, verbose_name='Place')),
                ('quali', models.CharField(max_length=50, verbose_name='Qualification')),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('job', models.CharField(max_length=50, verbose_name='Appointed as')),
                ('status', models.CharField(choices=[('EN', 'EN'), ('R', 'Rejected'), ('E', 'Appoint')], default='EN', max_length=50, verbose_name='Application Status')),
                ('rcode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='srto.rtoffice')),
            ],
        ),
        migrations.CreateModel(
            name='Dealers',
            fields=[
                ('dcode', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Dealer Code')),
                ('dname', models.CharField(max_length=100, verbose_name='Dealers Name')),
                ('place', models.CharField(max_length=100, verbose_name='Building Address')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone No')),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('DN', 'DN'), ('R', 'Rejected'), ('D', 'Approved')], default='DN', max_length=50, verbose_name='Application Status')),
                ('rcode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='srto.rtoffice')),
            ],
        ),
    ]
