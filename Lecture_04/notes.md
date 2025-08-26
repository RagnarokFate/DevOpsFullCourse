docker-compose --version
Messages addressed to "meeting group chat" will also appear in the meeting group chat in Team Chat
Due to the large number of participants in this meeting, system messages for those who joined or left have been disabled

Elad Shalev 7:07 PM
MONGO_INITDB_ROOT_USERNAME=admin
-e MONGO_INITDB_ROOT_PASSWORD=password
elad0>docker run -d -p 27017:27017 --name mongodb --network mongo-network -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password mongo

Elad Shalev 7:14 PM
-e ME_CONFIG_MONGODB_SERVER=mongodb
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin
-e ME_CONFIG_MONGODB_ADMINPASSWORD=password
-e ME_CONFIG_MONGODB_AUTH_DATABASE=admin
docker run -d -p 8080:8081 --network mongo-network --name mongo-express -e ME_CONFIG_MONGODB_SERVER=mongodb -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin -e ME_CONFIG_MONGODB_ADMINPASSWORD=password -e ME_CONFIG_MONGODB_AUTH_DATABASE=admin mongo-express


docker-compose.yaml

Elad Shalev 7:44 PM
version: "3"
services:
  mongodb:
    image: mongo:latest
    ports:
      - "27017:27017"
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=password
    networks:
      - mongo_network
  mongo-express:
    image: mongo-express:latest
    ports:
      - "8080:8081"
    environment:
      - ME_CONFIG_MONGODB_SERVER=mongodb
      - ME_CONFIG_MONGODB_PORT=27017
      - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
      - ME_CONFIG_MONGODB_ADMINPASSWORD=password
      - ME_CONFIG_MONGODB_AUTH_DATABASE=admin
    networks:
      - mongo_network
    depends_on:
      - mongodb
networks:
  mongo_network:
    driver: bridge