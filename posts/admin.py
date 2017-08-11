from django.contrib import admin
from  .models import   Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
       list_display = ["title","update", "timestamp"]
       list_display_links = ["update"]
       list_filter = ["title", "update"]
       search_fields = ["title","content"]
       list_editable = ["title"]
       # note you cannot have list_editable and list_display_links with the same objects
       class Meta:
         model =Post
admin.site.register(Post,PostAdmin)
