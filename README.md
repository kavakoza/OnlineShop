#  Online shop Project

### Description
Online Shop is a web application that provides functionality for managing a product catalog and users. 
This project allows you to create, edit and delete products. 
Users can register, log in and manage their data.

### Technologies used
- Python
- Django
- Django Rest Framework
- PostgreSQL

### RUN Information
Follow these steps to run the project:
1. Clone the repository
> git clone https://github.com/yourusername/OnlineShop.git
2. Create a Virtual Environment with the following requirements
> pip install -r requirements.txt
3. Set up your configuration using `.env.SAMPLE`
4. Activate migrations
> python3 manage.py migrate
5. Run the server
> python3 manage.py runserver

You can now access at localhost:8000 in your browser to interact with it.

### Project structure
The project has the following structure:
- categories - Categories management application
- products - Application for product catalog
- users - User management application
- config - Project settings
- env - Environment files
- media - Media files (images, etc.)
- static - Static files (CSS, JavaScript)
- manage.py - Project management file
- requirements.txt - List of dependencies
