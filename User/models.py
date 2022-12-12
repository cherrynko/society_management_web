from django.db import models
from account.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver


DEPARTMENTS = (
    ('Human Resources', 'Human Resources') ,
    ('Finance and Legal','Finance and Legal' ),
    ('Events', 'Events'), 
    ('Marketing','Marketing'),
    ('Outreach','Outreach'),
    ('Design', 'Design'),
)
DEP_ID = (
    (10,10) ,
    (20,20 ),
    (30,30), 
    (40,40),
    (50,50) ,
    (60,60),
)
ROLES = (
    ('Member', 'Member') ,
    ('Director','Director' ),
    ('Executive Council', 'Executive Council'), 
    ('Assistant Director','Assistant Director'),
)
ROLE_ID = (
    (1,1) ,
    (2,2 ),
    (3,3), 
    (4,4),
)
# Create your models here.

class Role(models.Model):
    role_id = models.IntegerField(primary_key=True, choices=ROLE_ID)
    role_name = models.CharField(max_length=100,choices=ROLES, default='Member')
    max_people = models.IntegerField(blank=True, null=True)
    min_people = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.role_name}'

class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True, choices=DEP_ID)
    dept_name = models.CharField(max_length=100,choices=DEPARTMENTS,default='Human Resources')
    num_members = models.IntegerField(blank=True, null=True)
    num_directors = models.IntegerField(blank=True, null=True)
    num_ads = models.IntegerField(blank=True, null=True)
    acc_num = models.IntegerField(blank=True, null=True)
    total_bal = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return f'{self.dept_name}'


class Member(models.Model):
    member_id = models.IntegerField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=100, null=True)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    # dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    email_id = models.EmailField()
    birth_date = models.DateField(blank=True, null=True)
    role_name = models.ForeignKey(Role, on_delete=models.CASCADE)
    # role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.member_name}-{self.dept_name}'

class Director(models.Model):
    member_id = models.IntegerField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=100, null=True)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    # dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    email_id = models.EmailField()
    birth_date = models.DateField(blank=True, null=True)
    role_name = models.ForeignKey(Role, on_delete=models.CASCADE)
    # role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

class AssistantDirector(models.Model):
    member_id = models.IntegerField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=100, null=True)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    # dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    email_id = models.EmailField()
    birth_date = models.DateField(blank=True, null=True)
    role_name = models.ForeignKey(Role, on_delete=models.CASCADE)
    # role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.member_name}-{self.dept_name}'
    
    def __str__(self):
        return f'{self.member_name}-{self.dept_name}'


class EC(models.Model):
    member_id = models.IntegerField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=100, null=True)
    # dept_name = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    # dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    email_id = models.EmailField()
    birth_date = models.DateField(blank=True, null=True)
    role_name = models.ForeignKey(Role, on_delete=models.CASCADE)
    # role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.member_name}'

class Sponsor(models.Model):
    sponsor_id = models.IntegerField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    sponsor_name = models.CharField(max_length=100, null=True)
    # dept_name = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    # dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    email_id = models.EmailField()
    
    def __str__(self):
        return f'{self.sponsor_name}'

class Patron(models.Model):
    patron_id = models.IntegerField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    patron_name = models.CharField(max_length=100, null=True)
    # dept_name = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    # dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    email_id = models.EmailField()
    
    def __str__(self):
        return f'{self.patron_name}'


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            Member.objects.create(admin=instance)
        if instance.user_type==2:
            Director.objects.create(admin=instance)
        if instance.user_type==3:
            EC.objects.create(admin=instance)
        if instance.user_type==4:
            AssistantDirector.objects.create(admin=instance)
        if instance.user_type==5:
            Sponsor.objects.create(admin=instance)
        if instance.user_type==6:
            Patron.objects.create(admin=instance)

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.Member.save()
    if instance.user_type==2:
        instance.Director.save()
    if instance.user_type==3:
        instance.EC.save()
    if instance.user_type==4:
        instance.AssistantDirector.save()
    if instance.user_type==5:
        instance.Sponsor.save()
    if instance.user_type==6:
        instance.Patron.save()