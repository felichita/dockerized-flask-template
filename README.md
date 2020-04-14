# hello_world Web serivices

What is it?
--------------------------------------------

Implemented a trivial HTTP "Hello, world!" web application in python
Requirements:
- Dockerfile that dockerizes the application.
- The app has a health-check.
- The application must provide metrics endpoint for Prometheus.
- Grafana dashboard with metrics visualization.
- docker-compose.yml that launches the app with all the necessary environment (Prometheus and Grafana).

How build from Dockerfile?
--------------------------------------------
DOCKER_BUILDKIT=1 docker build --ssh default --no-cache -t hello_world:latest -f Dockerfile .

How run docker-compose?
--------------------------------------------
docker-compose up

How can I deploy this app in kubernetes? (Not the best method)
--------------------------------------------
cat build/ansible/README.md
