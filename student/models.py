from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here.
GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female')
]

CASTE_CHOICES = [
    ('SC','SC'),
    ('ST','ST'),
    ('OBC','OBC'),
]

class Student(models.Model):
    Photo = models.ImageField(null=True, blank=True,upload_to='images', default='default.png')
    Name = models.CharField(max_length=200)
    Enrollment_No = models.CharField(max_length=10, null=True, blank=True)
    Course = models.ForeignKey('Courses', on_delete=models.DO_NOTHING)
    DOB = models.DateField(null=True, blank=True)
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES ,null=True, blank=True)
    Caste = models.CharField(max_length=20, choices=CASTE_CHOICES ,null=True,blank=True)
    Father_Name = models.CharField(max_length=200,null=True, blank=True)
    Mother_Name = models.CharField(max_length=200,null=True, blank=True)
    Contact_No = models.CharField(max_length=10,null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    District = models.CharField(max_length=20,null=True,blank=True)
    Address = models.TextField(null=True, blank=True)
    Highest_Qualification = models.CharField(max_length=30,null=True,blank=True)
    Name_Of_School = models.CharField(max_length=50,null=True, blank=True)
    Name_Of_Board = models.CharField(max_length=50,null=True, blank=True)
    Year_Of_Pass = models.CharField(max_length=10,null=True, blank=True)
    Marks_Obtained = models.CharField(max_length=10,null=True, blank=True)
    Total_Fees = models.IntegerField(null=True, blank=True)


    Date_Of_Admission = models.DateField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
    

    
class Courses(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Description = RichTextUploadingField()
    Duration = models.CharField(max_length=50,default='Months',null=True, blank=True)
    Eligibility = models.CharField(max_length=50,null=True, blank=True)
    Course_Fees = models.IntegerField(null=True, blank=True)
    Admission_Fee = models.IntegerField(null=True, blank=True)
    Fees_Structure = models.CharField(max_length=50,null=True, blank=True)
    

    def __str__(self):
        return self.Name
    
    # def __str__(Eligibility):
    #     return Eligibility
    

RECEIVER_CHOICES = [
    ('Somnath Chattejee','Somnath Chattejee'),
    ('Ayan Dhali','Ayan Dhali')
]

REMARKS_CHOICES = [
    ('Admission Fee','Admission Fee'),
    ('1st Installment','1st Installment'),
    ('2nd Installment','2nd Installment'),
    ('3rd Installment','3rd Installment'),
    ('4th Installment','4th Installment'),
    ('5th Installment','5th Installment'),
    ('6th Installment','6th Installment'),
    ('7th Installment','7th Installment'),
    ('8th Installment','8th Installment'),
    ('9th Installment','9th Installment'),
    ('10th Installment','10th Installment'),
    ('11th Installment','11th Installment'),
    ('12th Installment','12th Installment'),
]

PAYMENT_CHOICES=[
    ('Paid','Paid'),
    ('partially Paid','Partially Paid'),
]

class Fees_Payment(models.Model):
    Student = models.ForeignKey('Student', on_delete=models.CASCADE)
    Emi = models.IntegerField(null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Status = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    Remarks = models.CharField(max_length=50,choices=REMARKS_CHOICES,null=True,blank=True)
    Receiver = models.CharField(max_length=50,choices=RECEIVER_CHOICES, null=True,blank=True)
    Due = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.Student.Name
    

class Fees_Show(models.Model):
    Student = models.ForeignKey('Student', on_delete=models.CASCADE)
    Remarks = models.CharField(max_length=50,choices=REMARKS_CHOICES ,null=True,blank=True)
    Amount = models.IntegerField(null=True, blank=True)
    Emi_Payment_Date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.Student.Name + "  " + self.Remarks
    

class Enquries(models.Model):
    Name = models.CharField(max_length=60,blank=True,null=True)
    Course_Interest = models.ForeignKey('Courses', on_delete=models.DO_NOTHING)
    Address = models.TextField(null=True,blank=True)
    Mobile_No = models.CharField(max_length=10,blank=True,null=True)
    Whatsapp_No = models.CharField(max_length=10,blank=True,null=True)
    Email = models.EmailField(null=True, blank=True)
    Remarks = models.TextField(null=True,blank=True)
    Date = models.DateField(auto_now_add=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name


PMETHOD_CHOICES=[
    ('Cash','Cash'),
    ('Bank','Bank'),
]



class Transaction(models.Model):
    Date = models.DateField()
    Purpose = models.TextField()
    P_method = models.CharField(max_length=20,choices=PMETHOD_CHOICES)
    Amount = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Purpose
    

class Account(models.Model):
    a_id = models.IntegerField(default=1)
    Transaction = models.ForeignKey('Transaction',on_delete=models.DO_NOTHING,null=True,blank=True)
    Balance = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True,default=0)

    def __str__(self):
        return str(self.Balance)