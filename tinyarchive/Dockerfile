FROM python:alpine


#Apt get all the c libraries that Pillow needs to compile against
#also get gcc.

RUN apk add --update build-base tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev

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
