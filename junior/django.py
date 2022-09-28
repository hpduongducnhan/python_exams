



async def create_source_file_structure():
    """
    With Django
    create a simple web app that has two subapp: user and blog
        user: manage authenticated user, only authenticated user could access app
        blog: manage authenticated user's posts

    could use mariadb or postgresql 
    keep things simple!
    
    Time: 120 mins
    """

async def authentication():
    """
    Implement JWT authentication with Django dependency 
    to create web app which has authentication system with Password and Bearer
    
    Time: 60 mins
    """

async def authorization():
    """
    With Django framework,
    create a simple web app that has authorization system (django.contrib)
    web app has 3 api endpoints, each endpoint need a seperated permission

    Time: 120 mins
    """

async def middleware():
    """
    With Django framework, 
    create a simple web app that has a middleware to log to a file total time to process a request 
    
    Time: 60 mins
    """

async def background_tasks():
    """
    With Django framework, 
    create a simple web app that use background task to send amount of emails 
    when api is trigged
    
    Time: 60 mins
    """

async def serve_files():
    """
    With Django framework, 
    create a simple web app that could upload images, mp3 then download again
    web app has 2 api, one for upload files, one for download files
    web app must have authentication system, only authenticated user could upload/download their own files
    web app must have authorization system, 2 roles admin and normal_user, 
        admin could access all files
        normal_user only access their own files
    
    Time: 120 mins
    """


async def deployment():
    """
    With Django framework, gunicorn, 
    create a simple backend web app, then deploy using gunicorn, uvicorn
    web app could log access request, error request to file and to console
    web app has request timeout = 180s
    web app has 4 concurrent workers
    
    Time: 120 mins
    """