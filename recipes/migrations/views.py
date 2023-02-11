from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required,client_passes_test
from django.contrib import messages
from django.conf import parametres


#Cette fonction gère la vue d'inscription. Elle utilise la fonction render de Django pour afficher un modèle nommé /signup.html.
def signup(request):
    return render(request, '/signup.html')

#Cette fonction gère la vue d'accueil. Elle utilise la méthode objects.all() pour récupérer tous les objets de la classe Article du modèle models.
#Elle vérifie ensuite s'il existe un cookie nommé articles_ids. S'il existe, elle sépare les identifiants d'article dans le cookie en utilisant la méthode split('|') et compte le nombre d'articles en utilisant len(set(counter)).
#Si le cookie n'existe pas, la variable articles_count_in_cart est définie sur 0.
#La fonction vérifie également si l'utilisateur actuel est authentifié en utilisant request.clientis_authenticated. Si l'utilisateur est authentifié, la vue redirige l'utilisateur vers une autre vue nommée afterlogin.
#Enfin, la fonction utilise la fonction render pour afficher un modèle nommé /index.html. Elle passe également un contexte avec les articles et le nombre d'articles dans le panier à ce modèle pour les rendre dispon
def home_view(request):
    articles=models.Article.objects.all()
    if 'articles_ids' in request.COOKIES:
        articles_ids = request.COOKIES['articles_ids']
        counter=articles_ids.split('|')
        articles_count_in_cart=len(set(counter))
    else:
        article_count_in_cart=0
    if request.client.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'/index.html',{'articles':articles,'articles_count_in_cart':articles_count_in_cart})


#La fonction importe les formulaires ClientUserForm et ClientForm depuis un module appelé forms.
#La vue vérifie ensuite si la méthode de la requête est un formulaire POST en utilisant request.method. Si c'est le cas, elle crée des instances de ClientUserForm et ClientForm à partir des données du formulaire envoyé.
#La vue utilise ensuite la méthode is_valid pour vérifier que les données du formulaire sont valides. Si les données sont valides, elle enregistre d'abord les données de l'utilisateur en utilisant la méthode save. Ensuite, elle utilise la méthode set_password pour définir un mot de passe pour l'utilisateur, puis l'enregistre en utilisant la méthode save.
#Enfin, la vue enregistre les données du client en utilisant la méthode save de ClientForm, en passant commit=False pour indiquer que les données ne doivent pas être enregistrées immédiatement. La vue définit également la relation entre l'utilisateur et le client en définissant la propriété client de l'objet client sur l'objet utilisateur. Elle enregistre finalement les données du client en utilisant la méthode save.
def client_signup_view(request)
    clientForm=forms.ClientUserForm()
    clientForm=forms.ClientForm()
    if request.method=='POST'
        clientForm=forms.ClientUserForm(request.POST)
        clientForm=forms.ClientForm(request.POST,request.FILES)
        if clientForm.is_valid() and clientForm.is_valid()
            client=userForm.save()
            client.set_password(client.password)
            client.save()
            client=clientForm.save(commit=False)
            client.client=client
            client.save()


#cette fonction permet d'afficher tous les avis enregistrés dans la base de données. La décoration "@login_required" exige que l'utilisateur soit connecté pour accéder à cette vue. Si l'utilisateur n'est pas connecté, il sera redirigé vers la page d'identification spécifiée par "login_url='adminlogin'".
#Dans la vue, nous récupérons tous les objets du modèle "avis" à partir de la base de données et les classons par ordre décroissant d'identifiant (commande_by('-id')). Enfin, nous passons ces avis à la template "/view_avis.html" pour les afficher.
@login_required(login_url='adminlogin')
def view_avis_view(request):
    avis=models.avis.objects.all().commande_by('-id')
    return render(request,'/view_avis.html',{'avis':avis})

#Cette fonction ajoute un article à un panier. Elle commence par récupérer tous les articles de la base de données. Ensuite, elle vérifie s'il y a déjà des articles dans le panier en vérifiant les informations de cookie. Si oui, elle décompte le nombre d'articles dans le panier. Sinon, elle met à jour le nombre d'articles dans le panier à 1.
#Ensuite, elle renvoie la page d'index en envoyant les informations sur tous les articles et sur le nombre d'articles dans le panier. Enfin, elle met à jour les informations de cookie en ajoutant le nouvel article au panier et en affichant un message informant l'utilisateur que l'article a été ajouté au panier.
def add_to_cart_view(request,pk):
    articles=models.articles.objects.all()

    if 'articles_ids' in request.COOKIES:
        articles_ids = request.COOKIES['articles_ids']
        counter=articles_ids.split('|')
        articles_count_in_cart=len(set(counter))
    else:
        articles_count_in_cart=1

    response = render(request, '/index.html',{'articles':articles,'articles_count_in_cart':articles_count_in_cart})


    if 'articles_ids' in request.COOKIES:
        articles_ids = request.COOKIES['articles_ids']
        if articles_ids=="":
            articles_ids=str(pk)
        else:
            articles_ids=articles_ids+"|"+str(pk)
        response.set_cookie('articles_ids', articles_ids)
    else:
        response.set_cookie('articles_ids', pk)

    articles=models.articles.objects.get(id=pk)
    messages.info(request, articles.name + ' ajouté au panier!')

    return response

#La fonction cart_view affiche les produits dans le panier d'un utilisateur. Elle vérifie tout d'abord si le cookie articles_ids existe dans la requête request. Si oui, cela signifie que le panier de l'utilisateur contient déjà des produits. Le cookie articles_ids est alors divisé en une liste en utilisant la méthode split() avec '|' comme paramètre. La longueur de cette liste est ensuite calculée en utilisant la méthode len() avec set() comme paramètre. Le résultat est stocké dans la variable articles_count_in_cart.
#Si le cookie n'existe pas, alors la variable articles est définie sur None et la variable total est définie sur 0. Si le cookie existe, les produits associés aux identifiants présents dans articles_ids sont récupérés en utilisant le modèle articles et les méthodes all() et filter(). Pour chaque produit dans articles, son prix est ajouté à la variable total.
#Enfin, la fonction retourne un rendu de la vue /cart.html avec les variables articles, total et articles_count_in_cart en tant que contextes.
def cart_view(request):
    if 'articles_ids' in request.COOKIES:
        articles_ids = request.COOKIES['articles_ids']
        counter=articles_ids.split('|')
        articles_count_in_cart=len(set(counter))
    else:
        articles = None
        total = 0
        if 'articles_ids' in request.COOKIES:
            articles_ids = request.COOKIES['articles_ids']
            if articles_ids != "":
                articles_id_in_cart = articles_ids.split('|')
                articles = models.articles.objects.all().filter(id__in=articles_id_in_cart)
                for p in articles:
                    total = total + p.price
        return render(request, '/cart.html',
                      {'articles': articles, 'total': total, 'articles_count_in_cart': articles_count_in_cart})



#Cette fonction "send_avis_view" permet d'envoyer un avis sur un produit. Elle utilise un formulaire "avisForm" pour récupérer les informations saisies par l'utilisateur.
#Si la méthode est "POST" (c'est-à-dire que l'utilisateur a soumis le formulaire), alors on valide les données du formulaire avec "avisForm.is_valid()". Si les données sont valides, on enregistre les données avec "avisForm.save()".
#Enfin, la fonction renvoie un rendu de la page "send_avis.html" avec le formulaire "avisForm" pour afficher les données saisies par l'utilisateur.
def send_avis_view(request):
    avisForm=forms.avisForm()
    if request.method == 'POST':
        avisForm = forms.avisForm(request.POST)
        if avisForm.is_valid():
            avisForm.save()
    return render(request, '/send_avis.html', {'avisForm':avisForm})


