class Commande(models.Model):

    client=models.ForeignKey('Client', on_delete=models.CASCADE,null=True)
    Article=models.ForeignKey('Article',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    addresse = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    commande_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)