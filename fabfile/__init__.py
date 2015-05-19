from fabric.api import task, run, cd

# load ssl env
try:
    from local import *
except:
    pass


@task
def deploy():
    with cd('/var/www/msee'):
        run('bash scripts/build.sh')
