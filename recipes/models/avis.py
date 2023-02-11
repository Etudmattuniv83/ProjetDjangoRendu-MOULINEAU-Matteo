class Avis(models.Model):
    nom=models.CharField(max_length=40)
    avis=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.nom