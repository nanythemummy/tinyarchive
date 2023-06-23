FROM python:3.9

# Setup remote working directory into which the code ges copied.

WORKDIR /dighum150 

#Setup Pip and its requirements.

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#Copy in the code last so that can use caching and doesn't have to redownload the above
COPY tinyarchive/ .


#Run the test server
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
