from django.shortcuts import render
from catalog.models import Piece, Composer, PieceInstance, Genre


# Create your views here.
def index(request):
    """View function for home page"""

    # Generate counts of some of the main objects
    num_pieces = Piece.objects.all().count
    num_instances = PieceInstance.objects.all().count()

    # The 'all()' is implied
    num_composers = Composer.objects.count()

    context = {
        'num_pieces': num_pieces,
        'num_instances': num_instances,
        'num_composers': num_composers
    }

    return render(request, 'index.html', context=context)
