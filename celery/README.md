# Celery
task queue, to receive and send messages it uses another tool(a message broker)
celery instance or celery application
calling a task returns a  AsyncResult instance that can be used to check the state of the task, wait for the task to finish, get its return value or get an exception and its traceback
results are not enabled by default for that you need to configure a result backend
allows to reschedule or retry a task

celery -A {app} worker --loglevel=INFO

result = task.delay()
result.ready()
result.get(timeout=1)
    in case the task raised an exception, get() will re-raise the exception
result.traceback

to ensure resources are released, you must eventually call get() or forget() on every AsyncResult instance

configuration can be set on the app directly like app.conf.task_serializer = 'json' or app.conf.update(task_serializer='json')

app.config_from_object('name')  # name if often 'celeryconfig' and it is the name of a python script, where config are set as python variables

task_routes = {'tasks.add':'queue-name'}  # point a task to another queue
task_annotations = {'tasks.add': {'rate_limit': '10/m'}}  # only 10 tasks per minute

celery -A tasks control rate_limit tasks.add 10/m  # set a new rate limit for the task at runtime