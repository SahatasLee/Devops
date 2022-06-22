Docker 101

Ref.
-  https://medium.com/@rachatatongpagdee/docker-%E0%B8%84%E0%B8%B7%E0%B8%AD%E0%B8%AD%E0%B8%B0%E0%B9%84%E0%B8%A3-%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B9%84%E0%B8%A3-7e77145967b6
- https://medium.com/i-gear-geek/docker-%E0%B8%84%E0%B8%B7%E0%B8%AD-%E0%B9%80%E0%B8%A3%E0%B8%B4%E0%B9%88%E0%B8%A1%E0%B8%95%E0%B9%89%E0%B8%99%E0%B8%81%E0%B8%B1%E0%B8%9A-docker-56d0ba499ae8 


Docker network 
3 types of docker network
Bridge network
None network
Host network
Ref. https://medium.com/@somprasongd/docker-networking-59b6637de3df

Docker push
Ref. https://docs.docker.com/get-started/04_sharing_app/ 

Command :
สามารถย่อ id ให้เหลือแค่ unique id ที่สั้นที่สุดได้
 docker images 
// show all images

Docker build -t name-image . 
//  สร้าง image ชื่อตาม name-image โดยหาที่ไฟล์ /. 

docker run name-image/id-image 
// starts new container 

Docker ps -a 
// show all container

Docker history name-dockerimage 
// เรียกดู layer ของ image

Docker stop id-container/name-container
// stop running container สามารถย่อให้เหลือแค่ unique id ที่สั้นที่สุดได้

Docker rm id-container 
// remove container

Docker rmi id-image 
// remove image

Docker images prune
// remove all dangling images

Docker run —name name-container -d -p 8080:80 image:tag
// name container and map port

Docker run —name name-container -v $(pwd):/usr/share/nginx/html -d -p 8080:80 image:tag
// volume share data host and container bind volumes 

Docker run —name name-container -v $(pwd):/usr/share/nginx/html:ro -d -p 8080:80 image:tag
// volume share data host and container read only

docker exec -it website bash
// container bash  

Docker tag website:latest website:1
// set tag

 docker push YOUR-DOCKER-NAME/name-image:tag
// push image to registry

Docker  pull images-registry
// pull image from a registry

Docker inspect id-image/name-image
// inspect images for debug

Docker volume create data_volume
// 

Docker network  create option name-network
//

Docker network connect network container
//

sudo systemctl start docker

Systemctl start docker

systemctl status docker

Systemctl stop docker

Dockerd —debug

Sudo dockerd

Ref. Command : https://docs.docker.com/engine/reference/commandline/images/


Dockerfile
Ref. https://medium.com/i-gear-geek/%E0%B9%80%E0%B8%82%E0%B8%B5%E0%B8%A2%E0%B8%99-docker-file-%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B9%84%E0%B8%94%E0%B9%89-docker-image-d2dedd10361e


Docker-compose

Command 
`docker-compose up`: create and start containers
`docker-compose images`: show images
`docker-compose ps`: show container
`docker-compose stop`:  stop services
`docker-compose start`: start services
`docker-compose build`: build images

`docker-compose.yml`

```
version: '3'
services:
  wp_db:
    image: mariadb:10.1
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: wordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
wp:
    depends_on:
      - wp_db
    image: wordpress:latest
    ports:
      - "8080:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: wp_db:3306
      WORDPRESS_DB_PASSWORD: wordpress
pma:
    depends_on:
      - wp_db
    image: phpmyadmin/phpmyadmin
    links:
     - wp_db:db
    ports:
      - "8181:80"
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: wordpress
volumes:
  db_data:
      driver: local
```

- depend_on คือสั่งให้ service นั้นๆ เริ่มต้นการทำงานหลังจาก service ที่ depend on อยู่เริ่มต้นการทำงานเสร็จแล้ว

Ref. https://medium.com/touch-technologies/%E0%B8%97%E0%B8%B3%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B8%88%E0%B8%B1%E0%B8%81-docker-compose-b6688fc98c6f

https://medium.com/@somprasongd/docker-compose-%E0%B8%84%E0%B8%B7%E0%B8%AD-fc8b35e0c8bc


# Best practice docker
1. Use official docker image as base image
2. Use specific image versions
3. Use small-sized official images
4. Optimize caching image layers
5. Use .dockerignore to exclude files and folder
6. Make use of “Multi-stage builds”
7. Use the least privileged user
8. Scan your images for Vulnerabilities

docker run -d \
    --network mongo-network \
    --name mongo-express \
    -p 8081:8081 \
    -e ME_CONFIG_MONGODB_SERVER=“mongodb” \
    -e ME_CONFIG_BASICAUTH_USERNAME="user" \
    -e ME_CONFIG_BASICAUTH_PASSWORD="fairly long password" \
    mongo-express

