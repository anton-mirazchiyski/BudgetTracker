"""
URL configuration for budget_tracker project.
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from budget_tracker import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('budget_tracker.common.urls')),
    path('users/', include('budget_tracker.accounts.urls')),
    path('income/', include('budget_tracker.income.urls')),
    path('expenses/', include('budget_tracker.expenses.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
