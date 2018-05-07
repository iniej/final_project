from django.contrib import admin
from .models import UserInfo, WatchList, WatchedList
# Register the UserInfo, WatchList, and WatchedList models.
admin.site.register(UserInfo)
admin.site.register(WatchList)
admin.site.register(WatchedList)
