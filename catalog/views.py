from django.shortcuts import render
from catalog.models import Piece, Composer, PieceInstance, Genre
from django.views import generic
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    """View function for home page"""

    # Generate counts of some of the main objects
    num_pieces = Piece.objects.all().count
    # The 'all()' is implied
    num_composers = Composer.objects.count()
    num_genres = Genre.objects.count()

    context = {
        'num_pieces': num_pieces,
        'num_genres': num_genres,
        'num_composers': num_composers
    }

    return render(request, 'index.html', context=context)


class PieceListView(generic.ListView):
    model = Piece


class ComposerListView(generic.ListView):
    model = Composer


class PieceDetailView(generic.DetailView):
    model = Piece


class ComposerDetailView(generic.DetailView):
    model = Composer


def piece_detail_view(request, primary_key):
    piece = get_object_or_404(Piece, pk=primary_key)
    return render(request, 'catalog/piece_detail.html', context={'piece': piece})


class RecordingDetailView(generic.DetailView):
    model = Piece


def recording_detail_view(request, pk):
    piece = get_object_or_404(Piece, pk=pk)
    return render(request, 'catalog/recording_detail.html', context={'piece': piece})