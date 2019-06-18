# Gallery
###### Description
This is an application that tracks my gallery and allows users to view my photos and also copy the links of the photos.
Currently the admin is the only one with perimisions to edit the photos or make any form of changes to the application.
###### Author
Maurine Sinami

### Application Functionality
you can:

1. View different photos that interest you.
2. Click on a single photo to expand to view details of the image.
3. Search for different categories of photos and view them as well
4. View photos based on the location they were taken or category.

### Installations

1. Clone the repository with:
`git clone https://github.com/maurinesinami/gallery`
2. You will then have to unzip the zipped format of the repo
3. You will need to install all dependencies by running this command:
*first make sure your requirements.txt file is like this
`config==0.3.9`
`dj-database-url==0.5.0`
`Django==1.11`
`django-bootstrap3==10.0.1`
`django-heroku==0.3.1`
`gunicorn==19.9.0`
`Pillow==5.2.0`
`psycopg2==2.7.5`
`python-decouple==3.1`
`pytz==2018.5`
`whitenoise==4.0`
`pip install -r requirements.txt`
* if not use this command:
`pip freeze > requirements.txt`

4. To use the application locally you wil have to create a postgress database
follow these steps to get the app up and running:
* in your psql:
`CREATE DATABASE gallery;`
* in your terminal migrate with:
`python3.6 manage.py migrate`
* serve the application with:
`python manage.py runserver`
* open the app on localhost:8000

## Technologies used
1. Django 1.11
2. Python3.6
3.  HTML and Css
## Known Bugs
NO known Bugs.
## Behavior Driven Development

| Behaviour| Input | Output |
| ------------- | ----------------- | ------------------ |
| Display all photos on database  | "https://app-name@heroku.com"   | Loads all photos  |
| Save uploaded images | Upload image | Saves image |

| Show image details and image in full | Click image | Zooms with a modal |
| Search by category| search category| returns images on that specific category' |
## License
This project is licensed under the MIT Open Source license, (c) Maurine Sinami