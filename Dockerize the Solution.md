
1. Simple build with no volumes, image runs as it is      --------------------------------------

    docker build . -t bike_sharing:v1               # build image;  . for current folder,  -t for tag. v1 is the version tag. If omitted, Docker defaults to latest. 
    docker images                                   # list images
    docker images  | grep -i bike                   # -i: ignores the letter case.
    docker run -it bike_sharing:v1                  # OR
    
    docker run -itd bike_sharing:v1                 #  In the command docker run -itd:
                                                    #    -i: Interactive mode, allowing input.
                                                    #    -t: Allocates a pseudo-terminal.
                                                    #    -d: Detached mode; container runs in the background.

Thus, docker run -itd starts an interactive container session running detached, letting the container operate independently in the background.                                                   

    docker ps -a                                    # containers, -a for all even the stopped  

    # run docker and bash
    docker run -itd bike_sharing:v1 bash
    docker exec -it <container id> bash              # new interactive bash shell session inside the already-running Docker container.
    docker exec -it <container id> python main.py

    exit                                             # terminates that specific shell session, returning you to your original terminal or environment                      

    docker rm -f <contaier_id>                       # remove , -f to force , as container is running. or first stop it by 
    docker stop <container_id_or_name>


2. data loaded from volume , adds ./data to dockerignore and mount data folder to app/data on container                         
   echo "./data" >> .dockerignore                            # Appends ./data to .dockerignore, creating the file if it doesn't exist.
   docker build . -t bike_sharing:v2
   docker run -it -v ./data/:/app/data bike_sharing:v2       # would not work in gitbash
   # on windows you should run wth full path
   docker run -it -v "C:\work\Mlops\Model Deployment\Exercise\Bike_Sharing\data":/app/data bike_sharing:v2 bash
   winpty docker run -it -v "$(pwd)/data":/app/data bike_sharing:v2 bash


3. config file loaded from volume . now both folder data and file config are in ignore and should be mounted                        
   echo "config.py" > .dockerignore                  # Appends ./data to .dockerignore, creating the file if it doesn't exist.
   docker build . -t bike_sharing:v3
   docker run -it -v "$(pwd)/data":/app/data  -v "$(pwd)/config.py":/app/config.py  bike_sharing:v3 bash   # now both data and config are mounted

   docker run -it --mount type=bind,source="$(pwd)/config.py",target=/app/config.py bike_sharing:v3


5. push to dockerhub (used Lev's lectures)
    1. run container with mysql , sow hot to use env variables
        docker rm -f mysql-docker-local
        docker run -p 13306:3306 --name mysql-docker-local -e MYSQL_ROOT_PASSWORD=Password -d mysql:latest
        docker exec -it b67bf66e44c128647cc008552e55946dfb1b52d5f18cea189c1f81826ec0c5fd bash
        env
    2. how to push image to dockerhub
       docker tag bike_sharing:v3 313733172/bike_sharing:v3
       docker tag bike_sharing:v2 313733172/bike_sharing:v2
       docker tag bike_sharing:v1 313733172/bike_sharing:v1
       docker login 
       docker push 313733172/bike_sharing:v3

    3. run on  https://labs.play-with-docker.com/   
        docker login -u 313733172
        docker pull 313733172/bike_sharing:v1


