















Error 
1. data/output.csv permission denied

    solution :
    ```bash
        ls -ld /home/izzhamburhan/DE-football/data #check user
        sudo chown -R izzhamburhan:izzhamburhan /home/izzhamburhan/DE-football/data # change user
        chmod u+w /home/izzhamburhan/DE-football/data #update permission
    ```