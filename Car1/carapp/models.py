from django.db import models

# Create your models here.



class buyertelmanage(models.Manager):
   def charu(self,buytel):
       buycaruser(buyertel=buytel).save()

class usemanage(models.Manager):
    pass

class adminmanage(models.Manager):
    pass

class carmanage(models.Manager):

   def insert(self,pingpai,chexi,chexin,licheng,pailiang,biansuxiang,spsj,spd,price,zws,rylx,chezhu):
        cardetail(pingpai=pingpai,chexi=chexi,chexin=chexin,licheng=licheng,pailiang=pailiang,biansuxiang=biansuxiang,spsj=spsj,spd=spd,price=price,zws=zws,rylx=rylx,chezhu=chezhu).save()
        return "你的汽车已上传，瓜子二手车工作人员会第一时间联系你，进行汽车审核"




class User(models.Model):
    usu=usemanage()

    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=50)
    tel=models.CharField(max_length=50)
    lie1 = models.CharField(max_length=50)
    lie2 = models.CharField(max_length=50)
    lie3 = models.CharField(max_length=50)
    lie4 = models.CharField(max_length=50)
    lie5 = models.CharField(max_length=50)


class admin(models.Model):
    adm=adminmanage()
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)


class cardetail(models.Model):
    car=carmanage()
    pingpai=models.CharField(max_length=50)
    chexi=models.CharField(max_length=50)
    chexin=models.CharField(max_length=50)
    licheng=models.CharField(max_length=50)
    pailiang=models.CharField(max_length=50)
    biansuxiang=models.CharField(max_length=50)
    spsj=models.CharField(max_length=50)
    spd=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    zws=models.CharField(max_length=50)
    rylx=models.CharField(max_length=50)
    chezhu=models.CharField(max_length=50)
    lie1=models.CharField(max_length=50)
    lie2=models.CharField(max_length=50)
    lie3=models.CharField(max_length=50)
    lie4=models.CharField(max_length=50)
    lie5=models.CharField(max_length=50)


class buycaruser(models.Model):
    btel=buyertelmanage()
    buyertel=models.CharField(max_length=20)
