from django.db import models

# Create your models here.
class Category(models.Model):
    STATUS = (
        ('True','Mavjud'),
        ('False','Mavjud emas'),
    )
    categories = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Media/categ_img')
    izoh = models.TextField()
    status = models.CharField(choices=STATUS,max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categories


class Mahsulot(models.Model):
    STATUS = (
        ('True','Mavjud'),
        ('False','Mavjud emas'),
    )
    kategoriya = models.ForeignKey(Category,on_delete=models.CASCADE)
    sotuv = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Media/mah_img')
    mah_nomi = models.CharField(max_length=80)
    status = models.CharField(choices=STATUS,max_length=20)
    yangi_narx = models.DecimalField(null=True,max_digits=10,decimal_places=4)
    eski_narx = models.DecimalField(null=True,max_digits=10,decimal_places=4)

    def __str__(self):
        return self.mah_nomi



class Main(models.Model):
    title = models.CharField(max_length=50)
    title2 = models.CharField(max_length=80)
    title3 = models.CharField(max_length=80)
    summary = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Media/main_img')
    def __str__(self):
        return self.title


class FeaturedBrand(models.Model):
    image = models.ImageField(upload_to='Media/brand_img')
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class FromBlog(models.Model):
    STATUS = (
        ('True','Mavjud'),
        ('False','Mavjud emas'),
    )
    image = models.ImageField(upload_to='Media/blog_img')
    status = models.CharField(choices=STATUS, max_length=20)
    slug = models.SlugField(max_length=20)
    brand_name = models.CharField(max_length=50)
    izoh = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    views = models.CharField(max_length=100)
    def __str__(self):
        return self.izoh


class Sale(models.Model):
    STATUS = (
        ('True','Mavjud'),
        ('False','Mavjud emas'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Media/sale_img')
    status = models.CharField(choices=STATUS,max_length=20)

    def __str__(self):
        return self.title


class Belowfooter(models.Model):
    mah_nomi = models.CharField(max_length=80)
    image = models.ImageField(upload_to='Media/mah_img')
    yangi_narx = models.CharField(max_length=50)
    eski_narx = models.CharField(max_length=50)

    def __str__(self):
        return self.mah_nomi


class Footermodel(models.Model):
    logo = models.ImageField(upload_to='Media/logo_img')
    title = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=100)
    hours = models.CharField(max_length=200)
    follow = models.CharField(max_length=70)
    fac_logo = models.TextField()
    twit_logo = models.TextField()
    ins_logo = models.TextField()
    you_logo = models.TextField()

    def __str__(self):
        return self.title


class Appstore(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    app_store = models.CharField(max_length=200)
    google_play = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Aboutmain(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    text = models.TextField()
    image = models.ImageField(upload_to='Media/about_img')

    def __str__(self):
        return self.title

class Team(models.Model):
    image = models.ImageField(upload_to='Media/team_img')
    name = models.CharField(max_length=50)
    kasbi = models.CharField(max_length=100)
    fac_logo = models.CharField(max_length=200)
    twit_logo = models.CharField(max_length=200)
    ins_logo = models.CharField(max_length=200)
    you_logo = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='Media/comment_img')

    def __str__(self):
        return self.name

class EvaraCorp(models.Model):
    image = models.ImageField(upload_to='Media/pic_img')
    place = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.place


class InContact(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class CategoryBlog(models.Model):
    STATUS = (
        ('True','Mavjud'),
        ('False','Mavjud emas'),
    )
    categories = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS,max_length=20)

    def __str__(self):
        return self.categories

class OurBlog(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    status = models.CharField(choices=STATUS, max_length=20)
    kategoriy = models.ForeignKey(CategoryBlog,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Media/ourblog_img')
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    views = models.CharField(max_length=100)

    def __str__(self):
        return self.title