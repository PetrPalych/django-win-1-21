from django.db import models


# Create your models here.


class Book(models.Model):
    GENRE = (
        ('Жанр', 'Жанр'),
        ('Боевик', 'Боевик'),
        ('Романтика', 'Романтика'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.SmallIntegerField()
    image = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, default=GENRE[0], null=True)

    def __str__(self):
        return self.title


class ReviewBook(models.Model):
    STARS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),
    )

    title_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_object')
    text_review = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=STARS)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий к {self.title_book}"
