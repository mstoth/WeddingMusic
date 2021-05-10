from django.contrib import admin

# Register your models here.
from .models import Composer, Genre, Piece, PieceInstance

# admin.site.register(Piece)
# admin.site.register(Composer)
admin.site.register(Genre)
# admin.site.register(PieceInstance)

class ComposerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', \
	'date_of_birth', 'date_of_death')
class PieceInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status','imprint' )
class PieceAdmin(admin.ModelAdmin):
    list_display = ('title', 'composer', 'display_genre')


admin.site.register(Composer,ComposerAdmin)
admin.site.register(Piece,PieceAdmin)
admin.site.register(PieceInstance,PieceInstanceAdmin)
