# Sistema Simples de Vendas

@Instalacao:
git clone https://github.com/renatocarcosta/tccVenddas.git

# No servidor
pip install django
pip install django_admin_bootstrapped
pip install unipath

# Config no NGIX
```config
location /static {
        proxy_pass http://localhost:8888;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

  location /vendas {
        proxy_pass http://localhost:8888;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

