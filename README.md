
# Projet Django Multilingue
Ce projet Django est une application web multilingue permettant de gérer des articles de blog et d'intégrer des fonctionnalités avancées telles qu'un chatbot utilisant un modèle de langage et une recherche augmentée par intelligence artificielle (RAG).


# Installation
Pour exécuter ce projet localement, suivez ces étapes :

# Clonage du projet :
git clone https://github.com/Faizarouibahh/multilang_site.git
cd multilang_site
Installation des dépendances 

# Configuration de la base de données :
DATABASES = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'multilang_site',
        'USER': 'postgres',
        'PASSWORD': 'root', 
        'HOST': 'localhost',
        'PORT': '5432',
    }

## Appliquer les migrations :
python manage.py makemigrations
python manage.py migrate 

# Utilisation
Lancer le serveur de développement :
      python manage.py runserver
       Le site sera accessible à l'adresse http://localhost:8000.

Accès à l'interface d'administration :
Pour accéder à l'interface d'administration Django, créez un superutilisateur avec la commande :
python manage.py createsuperuser
Puis connectez-vous à http://localhost:8000/admin/ pour gérer les articles de blog et les utilisateurs.

Tester les fonctionnalités multilingues :
Explorez le site pour voir comment les articles sont présentés dans différentes langues (français et anglais).

# Fonctionnalités
# Gestion des articles :

Liste des articles avec titre, contenu et date de publication.
Création, mise à jour et suppression d'articles via l'API.

# Chatbot :

Utilisation d'un chatbot simple intégré à une vue Django.
### Utilisation
Pour tester le chatbot :

Lancez votre serveur Django.
Accédez à la page http://localhost:8000/chatbot/.
Saisissez un message dans le champ de texte et appuyez sur "Send".
Observez la réponse du chatbot affichée sous le formulaire.


