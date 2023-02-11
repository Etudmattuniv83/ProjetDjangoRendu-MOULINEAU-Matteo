class Client(models.Model):
    client=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/ClientProfilePic/',null=True,blank=True)
    addresse = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_nom(self):
        return self.user.prenom+" "+self.user.nom
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.prenom