echo "BUILD START"
pip install -requirements.txt
python manage.py collectstatic --noinput --clear
echo "BUILD END