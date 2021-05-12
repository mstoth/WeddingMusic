from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a piece style (e.g. Prelude, Postlude, Interlude)')

    def __str__(self):
        """Sting for representing the Model Object """
        return self.name



class Piece(models.Model):
    """Piece representing a piece of music """
    title = models.CharField(max_length=200, default='not set')
    composer = models.CharField(max_length=200, default='not set')
    publisher = models.CharField(max_length=200,default='not set')
    genre = models.ManyToManyField(Genre, help_text='Select a style for this piece')
    isbn = models.CharField('ISBN', max_length=13, unique=True,
    help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a> (if unknown, enter "unknown")')
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the piece')
    filename = models.CharField(max_length=200,default='not set')

    # Foreign Key used because piece can only have one composer, but composers can have multiple pieces
    # Composer as a string rather than object because it hasn't been declared yet in the file
    #    composer = models.ForeignKey('Composer', on_delete=models.SET_NULL, null=True)

    # ManyToManyField used because genre can contain many pieces. Pieces can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """Piece Model"""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('piece-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

import uuid # Required for unique book instances

class PieceInstance(models.Model):
    """Model representing a specific copy of a piece 
       (i.e. that can be downloaded from the library)."""
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          help_text='Unique ID for this particular piece across whole library')
    piece = models.ForeignKey('Piece', on_delete=models.PROTECT, null=True)
    imprint = models.CharField(max_length=200)

    LOAN_STATUS = (
        ('f', 'Free'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='f',
        help_text='Piece availability',
    )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.piece.title})'


class Composer(models.Model):
    """Model representing a composer."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          help_text='Unique ID for this particular piece across whole library')

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('composer-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
