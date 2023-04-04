# Airflow-Crash-Course
Crash course on airflow

## Installation

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

- Via docker, set approriate port

    ```curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.3/docker-compose.yaml'```

- Create user

    On Linux, the quick-start needs to know your host user id and needs to have group id set to 0. Otherwise the files created in dags, logs and plugins will be created with root user ownership. You have to make sure to configure them for the docker-compose:

```
    mkdir -p ./dags ./logs ./plugins

    echo -e "AIRFLOW_UID=$(id -u)" > .env
```

## Common commands

- Run airflow

    ```sudo docker compose up```

- View container details

    ```sudo docker exec -it 'container-name' /bin/bash```

- View files

    ```ls /bin/bash```

- Open psql shell

    ```psql -Uairflow```
    
Note : Use ctrl + d to exit
