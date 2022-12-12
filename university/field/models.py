from django.db import models
from django.contrib.auth.models import User
from twilio.rest import Client


# Create your models here.
class FieldApplication(models.Model):
	firstname = models.CharField(max_length=50)
	middlename = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	regno = models.CharField(max_length=50) 
	idara=(('computer_science',"computer science"),('computer_engineering',"computer engineering"))           
	department = models.CharField(max_length=50,choices=idara)
	masomo=(('certificate',"CERTIFICATE"),('diploma',"DIPLOMA"),('bachelor',"BACHELOR"))
	level = models.CharField(max_length=50,choices=masomo)
	tahasusi=(('computer_science',"computer science"),('computer_engineering',"computer engineering"),
		('data_science',"data science"),('cybersecurity',"cybersecurity")) 
	course = models.CharField(max_length=50,choices=tahasusi)
	mwaka=(('1st_year',"1st year"),('2nd_year',"2nd year"),('3rd_year',"3rd year"))
	year = models.CharField(max_length=50,choices=mwaka)
	mahali=(('mbeya_cement',"mbeya cement"),('ally_rich',"Ally Rich Ltd"),
		('tra_mbeya',"TRA Mbeya"),('mzumbe_university',"Mzumbe University")) 
	allocation = models.CharField(max_length=50,choices=mahali)
	phone_number = models.CharField(max_length=15,blank=True, null=True)
	approved = models.BooleanField('Approved',default=False)

	def __str__(self):
		return str(self.firstname)

	
	# def save(self, *args, **kwargs):
    #     #if test_result is less than 80 execute this
	# 	if self.approved == True:
    #         #twilio code
	# 		account_sid = 'ACcf0735bb3604a30f4482fa1fb923db94'
	# 		auth_token = '4b221ad700de5ca136caf0d6c4635a7c'
	# 		client = Client(account_sid, auth_token)

	# 		message = client.messages.create(
	# 		                            body=f'Hi, your test result is {self.firstname}. Great job',
	# 		                            from_='YOUR_TRIAL_NUMBER',
	# 		                            to='VERIFIED_NUMBER' 
	# 		                        )

	# 		print(message.sid)
	# 	return super().save(*args, **kwargs)

class Profile(models.Model):
	user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
	bio = models.TextField(max_length=500)

	def __str__(self):
		return str(self.user)



  		