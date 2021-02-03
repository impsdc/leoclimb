from django.contrib import admin
from .models import Accueil, DevinciClimbingContest

#making model unique
@admin.register(Accueil)
class AuthorAdmin(admin.ModelAdmin):

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False

#making model unique
@admin.register(DevinciClimbingContest)
class AuthorAdmin(admin.ModelAdmin):

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False