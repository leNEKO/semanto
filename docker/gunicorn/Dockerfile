FROM python:slim

# expose to nginx
EXPOSE 9000

ADD requirements.txt .

RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

CMD ["gunicorn", "--workers=5", "--threads=2", "--bind=0.0.0.0:9000", "codepen.app:app"]
