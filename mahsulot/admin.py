from django.contrib import admin
from mahsulot.models import Main, Category, Mahsulot, FeaturedBrand, FromBlog, Sale, \
    Belowfooter, Footermodel, Appstore, Aboutmain, Team, Comment, EvaraCorp, InContact, CategoryBlog, OurBlog


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['categories','izoh','image']
    list_filter = ['categories']


class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ['categories','status']
    list_filter = ['categories']


class MahsulotAdmin(admin.ModelAdmin):
    list_display = ['kategoriya','sotuv','image','mah_nomi','yangi_narx','eski_narx']
    list_filter = ['mah_nomi']


class MainAdmin(admin.ModelAdmin):
    list_display = ['title','title2','title3','summary','image']
    list_filter = ['title']

class FeaturedBrandAdmin(admin.ModelAdmin):
    list_display = ['image']
    list_filter = ['name']


class FromBlogAdmin(admin.ModelAdmin):
    list_display = ['image','status','slug','brand_name','izoh','views']
    list_filter = ['izoh']


class SaleAdmin(admin.ModelAdmin):
    list_display = ['title','description','image']
    list_filter = ['title']



class BelowfooterAdmin(admin.ModelAdmin):
    list_display = ['mah_nomi','image','yangi_narx','eski_narx']
    list_filter = ['mah_nomi']


class FootermodelAdmin(admin.ModelAdmin):
    list_display = ['logo','title','address','phone','hours','follow','fac_logo','twit_logo','ins_logo','you_logo']
    list_filter = ['title']


class AppstoreAdmin(admin.ModelAdmin):
    list_display = ['title','description','app_store','google_play']
    list_filter = ['title']


class AboutmainAdmin(admin.ModelAdmin):
    list_display = ['title','description','text','image']
    list_filter = ['title']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['image','name','kasbi','fac_logo','twit_logo','ins_logo','you_logo']
    list_filter = ['name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','nick_name','text','image']
    list_filter = ['name']


class EvaraCorpAdmin(admin.ModelAdmin):
    list_display = ['image','place','address']
    list_filter = ['place']


class InContactAdmin(admin.ModelAdmin):
    list_display = ['title','description','phone','email']
    list_filter = ['title']

class OurBlogAdmin(admin.ModelAdmin):
    list_display = ['kategoriy','image','title','text','views','date','status']
    list_filter = ['title']

admin.site.register(Main,MainAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(CategoryBlog,CategoryBlogAdmin)
admin.site.register(Mahsulot,MahsulotAdmin)
admin.site.register(FeaturedBrand,FeaturedBrandAdmin)
admin.site.register(FromBlog,FromBlogAdmin)
admin.site.register(Sale,SaleAdmin)
admin.site.register(Belowfooter,BelowfooterAdmin)
admin.site.register(Footermodel,FootermodelAdmin)
admin.site.register(Appstore,AppstoreAdmin)
admin.site.register(Aboutmain,AboutmainAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(EvaraCorp,EvaraCorpAdmin)
admin.site.register(InContact,InContactAdmin)
admin.site.register(OurBlog,OurBlogAdmin)
