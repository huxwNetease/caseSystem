from django.db import models

# Create your models here.
class WordMenu(models.Model):
    menuname = models.CharField(max_length=128, unique = True)  #目录名称
    menulevel = models.IntegerField(default=0)   #目录级别
    menuplevel = models.IntegerField(default=0)   #目录父级别（指向目录的id）

    def _str_(self):
        return self.menuname

    class Meta:
        verbose_name = "词条目录"
        verbose_name_plural = "词条目录"



class PictureMenu(models.Model):
    menuname = models.CharField(max_length=128, unique = True)  #目录名称
    menulevel = models.IntegerField(default=0)   #目录级别
    menuplevel = models.IntegerField(default=0)   #目录父级别（指向目录的id）

    def _str_(self):
        return self.menuname

    class Meta:
        verbose_name = "图片目录"
        verbose_name_plural = "图片目录"



class VoiceMenu(models.Model):
    menuname = models.CharField(max_length=128, unique = True)  #目录名称
    menulevel = models.IntegerField(default=0)   #目录级别
    menuplevel = models.IntegerField(default=0)   #目录父级别（指向目录的id）

    def _str_(self):
        return self.menuname

    class Meta:
        verbose_name = "音源目录"
        verbose_name_plural = "音源目录"




class HomeMenu(models.Model):
    menuname = models.CharField(max_length=128, unique = True)  #目录名称
    menulevel = models.IntegerField(default=0)   #目录级别
    menuplevel = models.IntegerField(default=0)   #目录父级别（指向目录的id）

    def _str_(self):
        return self.menuname

    class Meta:
        verbose_name = "主页目录"
        verbose_name_plural = "主页目录"