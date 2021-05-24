# KAFKA CLUSTER IN DOCKER WITH MONITORING SYSTEM (GRAFANA + PROMETHEUS)

The lab creates a kafka cluster made up of two functional nodes and a zookeeper manager. It also has monitoring using graphane and prometheus

## Description lab 🚀


The lab does not comply with good practices to be in production. As kafka images we use the ubuntu image so that the kafka installation is not transparent.


### Pre-requisitos 📋

Linux computer with:
* python3
* docker
* docker-compose
* lib-> confluent_kafka (to client python3 producer and consumer)

### Instalación 🔧

- git clone https://github.com/bsotob/kafka.git
- Edit the following property in the files:  advertised.listeners=PLAINTEXT://IP_DOCKER_HOST:909X   (command to extract it: ip addr show docker0 | grep -Po 'inet \K[\d.]+') and port defined in docker-compose : 9091,9092

          -   kafka_node_1/config/server.properties
          
          -   kafka_node_2/config/server.properties
          
- docker-compose build
- docker-compose up



## Accesos ⚙️

URL access grafana : http://localhost:3000/login

URL access prometheus: http://localhost:9000/targets

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.
