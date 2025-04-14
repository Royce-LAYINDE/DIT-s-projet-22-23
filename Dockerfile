# Utilisez une image Nginx comme base
FROM nginx:latest

# Copiez les fichiers du site web dans le répertoire de travail de Nginx
COPY . /usr/share/nginx/html

# Le conteneur Nginx écoute par défaut sur le port 80
EXPOSE 80

# Commande par défaut pour démarrer le serveur Nginx
CMD ["nginx", "-g", "daemon off;"]
