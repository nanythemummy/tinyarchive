FROM python:3.11 


#disable pip cache because we aren't going to need it, 
#and make it so that log messages show up immediately.
#This follows instructions on
# https://medium.com/vantageai/how-to-make-your-python-docker-images-secure-fast-small-b3a6870373a0

ENV PYTHONUNBUFFERED=1 \ 
    PIP_NO_CACHE_DIR=1

RUN set -ex \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*


# Setup remote working directory into which the code ges copied.
RUN mkdir /tinyarchive
WORKDIR /tinyarchive 

#Setup Pip and its requirements.

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#Copy in the code last so that can use caching and doesn't have to redownload the above
COPY . .

#Run the test server
EXPOSE 8000
#CMD tail -f /dev/null
CMD python manage.py runserver 0.0.0.0:8000
