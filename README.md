# drf-assgienment
The Backend assignment is given by **True Value Access LLP** for internship shortlisting.
This rest api is developed using django rest framework and can be test using browsable api

##Installation
1. Make Sure you have python version >=3.8 installed on your system.
2. Use package manager pip to install necessary packages for running projects

```bash
pip install django
pip install djangorestframework django-filter markdown
```
## Setup
1.Download or clone the github repository in your directory using git.
2. Run the commands shown below
```bash
git clone https://github.com/Vpb123/drf-assgienment.git
cd drf-assignment 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## Description
1. You can find get, post, put, patch and delete methods in views.py file.
2. Go to http://127.0.0.1:8000/userapi/ in your browser, you will find the browsable api where you can test all the requests.
3. You can go to http://127.0.0.1:8000/userapi/<int:pk>/ to get data of individual user where pk will be id of ther user eg. http://127.0.0.1:8000/userapi/1/
4. You can update the data of user partially, completely or can delete the user.
5. Pagination, limit, search and order filter is implemented where default limit is 5 i.e. it will return 5 entries.
6. To visit a particular page you can use http://127.0.0.1:8000/userapi/?page=3&limit=10&ordering=-age where page can have any value, set limit as desired and ordering or sorting can be done using any of the attribute either in ascending or descending order(use - for it)
7. You can search entries using first_name or last_name as follows: http://127.0.0.1:8000/userapi/?search=James, the search is case sensitive.
8. Example url of use of all features: http://127.0.0.1:8000/userapi/?page=1&limit=10&ordering=age&search=James
9. Don't use seach feature with a particular page, if entry is not found, it will result in invalid page.
10. You can test and explore through browsable api.
11. Sample data used from https://datapeace-storage.s3-us-west-2.amazonaws.com/dummy_data/users.json


   



