#!/builds/bin/bash
echo "Iniciando el despliegue automatico de Don Alberto"
cd /home/posadaleon/moto-api
git pull origin feature-inventario
source venv/bin/activate
sudo systemctl restart moto-api.service
sudo systemctl status moto-api.service