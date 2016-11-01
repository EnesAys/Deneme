from deneme.models import Deneme,Konu,Review
from django.contrib import admin

# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
class KonuAdmin(admin.ModelAdmin):
    list_display = ('Konu', 'User', 'Comment', 'Vote',
                    'review_count')
    inlines = [
        ReviewInline,
    ]

admin.site.register(Deneme)
admin.site.register(Konu)
admin.site.register(Review)
