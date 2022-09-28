
async def create_celery_worker():
    """
    With Celery framework
    
    create celery worker 
        mode prefork, 
        concurrent task each worker 10, 
        concurrent worker 4 

    keep things simple!
    
    Time: 60 mins
    """

async def create_celery_beat():
    """
    With Celery framework
    
    create celery beat with database scheduler 

    use postgresql or mariadb
    keep things simple!
    
    Time: 60 mins
    """


async def configure_celery_task_with_routing_system():
    """
    With Django framework,

    we have 2 task A and task B
    
    create celery worker A with queue A
        mode prefork, 
        concurrent task each worker 10, 
        concurrent worker 4 
        run only task A

    create celery worker B with queue B
        mode prefork, 
        concurrent task each worker 10, 
        concurrent worker 4 
        run only task B

    keep things simple!
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