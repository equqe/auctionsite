from django.db import models

class AuctionItem(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    finish_price = models.DecimalField(max_digits=10, decimal_places=2)
    auction_date = models.DateTimeField()

    def __str__(self):
        
        return self.name



class Auction(models.Model):
    AUCTION_TYPES = [
        ('classic', 'Классический аукцион'),
        ('blind', 'Закрытый аукцион'),
        ('dutch', 'Голландский аукцион'),
    ]

    auction_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    beneficiary = models.CharField(max_length=100)
    auction_type = models.CharField(max_length=10, choices=AUCTION_TYPES)
    description = models.TextField()
    address = models.CharField(max_length=255)
    contacts = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
