git pull
source /data/flasktest/venv/bin/activate
pip3 install -r requirements.txt
supervisorctl restart all
sudo service nginx reload