[WEEK 1]

**What I built:**

Installed WSL (Ubuntu) as it was easier to use and provided a better environment for development.

Installed Node.js to be able to execute JavaScript code outside the web browser. Installed Docker for later use in containerisation, allowing applications to be isolated while still running on the same host.

Set up Git and GitHub to keep a record of all technical and written updates made to the application and throughout the development process.

**Decisions I made and why:**

Using WSL (Ubuntu), the only strategic decision of why this was used instead of PowerShell is because of familiarisation with the commands of bash.

**What went wrong/How I fixed it:**

Firstly, an unexpected WSL issue was encountered when trying to update the Ubuntu user password as this was forgotten, the error indicated that WSL was not recognised. To troubleshoot the issue, it was verified whether WSL for Ubuntu was up to date via the Microsoft Store. The findings indicated that it was not, so I proceeded to update it and then restart the OS. This fixed the issue and the password could be reset.

Docker installation imposed a setback as when trying to install it, it exited throwing an error saying that Docker requires an elevated user to install. After some investigation, it was found that the issue was related to the ProgramData DockerDesktop folder having incorrect permissions from a previous failed installation. This was resolved by removing/resetting the DockerDesktop directory and running the installer again as Administrator, which allowed the installation to complete successfully.

While running the application, an error occurred stating that the module 'express' could not be found. This was due to dependencies not being installed. This was resolved by running 'npm install', which installed all required packages defined in package.json.

Additionally, npm reported several vulnerabilities within the dependencies. This was addressed by running 'npm audit fix', which updated the affected packages to more secure versions.

**Thoughts/Considerations:**

The application structure is quite simple and basic as it does not contain any frontend server or database, and currently consists only of a backend server.

The clear objective here is to transform it into a final web application that follows a three-tier structure.

Additionally, virtual machines will not be used for the development of this application, as that level of virtualisation would require more resources and dependencies. Instead, containerisation will be used. This is where Docker comes in, allowing each part of the application to be isolated within its own environment with its own dependencies, while still running on the same host system.

This approach also supports better scalability and aligns with cloud technologies, as containers can be deployed and managed more efficiently while sharing the same OS kernel.

The project aligns with a Software as a Service (SaaS) model, as it focuses on delivering a complete web application, while utilising infrastructure and platform-level concepts such as containerisation and orchestration.

[WEEK 2]

**What I built**

Built a staged deployment of an image with a smaller size than a traditional single-stage deployment. Alpine Linux was used for the second stage and non-required dependencies/packages were pruned so that only the necessary runtime components remained in the final image.

The logic behind staged deployment is that a smaller image size implies a faster container deployment while using fewer OS resources and less storage space. Additionally, the implementation of staged deployments increases scalability and cost efficiency within a company, as fewer computing resources are consumed and containers can be deployed faster on a single host.

It is also worth mentioning from a security perspective that reducing unnecessary packages lowers the attack surface, as fewer potential entry points are exposed to an attacker.

The Docker image size was verified after rebuilding the image and it was confirmed that the staged deployment significantly reduced the final image footprint compared to the original single-stage image.

**Thoughts/Considerations:**

Staged deployments should be preferred rather than treated as an optional implementation. They should be considered part of operational excellence procedures because they improve efficiency, scalability, and resource optimisation within an organisation or environment while also reducing unnecessary energy and storage consumption.

Another important consideration is that staged deployments separate the build environment from the runtime environment, allowing only the required application files and production dependencies to be included in the final image.

This approach also improves maintainability and portability, as the final runtime image becomes cleaner and easier to deploy consistently across different systems and cloud environments.

[WEEK 2]

**What I built:**

Installed PostgreSQL as the database for the deployment of the application. The cloud-native expansion of the application is broken down into three tiers: backend, database, and frontend. PostgreSQL was installed for the database layer.

A `todos` table was created inside the database and then both the backend and frontend were started using `npm start` to confirm functionality, networking, and database connectivity between the services.

**Decisions I made and why:**

Installed PostgreSQL with a custom password and used the default PostgreSQL port during installation for a faster setup and fewer networking modifications later on.

**What went wrong/How I fixed it:**

When PostgreSQL was first installed, a password was configured, however when trying to connect to the database the password authentication kept failing, therefore I could not access the database.

The solution chosen for this issue was to completely remove PostgreSQL and its remaining data folders and then perform a clean installation again. More advanced methods such as recovering or manually modifying authentication files would have taken longer and added unnecessary complexity for a fresh database with no important data stored inside.

After reinstalling PostgreSQL the login worked correctly.

Another issue encountered was related to backend/database connectivity. The frontend displayed a network/authentication related error message and the backend later failed with database connection errors.

After investigating the issue it was found that the `.env` configuration file contained the wrong database password and initially the wrong database connection context was also being used. PostgreSQL was defaulting to the `postgres` database while the backend application expected the `todo` database.

This was fixed by:
- Updating the `.env` file with the correct PostgreSQL password
- Connecting directly to the correct database using:

`psql -U postgres -h localhost -p 5432 -d todo`

- Creating the required `todos` table inside the correct database

After these corrections the backend and frontend communicated successfully and the application worked correctly.

**Thoughts/Considerations:**

Passwords configured within any environment should be stored somewhere secure and accessible only by the administrator in case authentication issues occur later on.

Another important consideration is that database servers can contain multiple databases, therefore creating a table inside one database does not automatically make it accessible from another one. This became important during troubleshooting because the backend application expected the `todo` database specifically.

The root issue with the original installation may also have been caused by a corrupted installation or authentication configuration, although this was not fully confirmed. Reinstalling PostgreSQL was the fastest and most practical solution in this situation.

[WEEK 2]

**What I built**

Composed a Dockerfile for both the frontend (web) and backend. These allow each part of the application to run inside isolated containers that contain their own dependencies and packages, reducing attack surface while also increasing scalability, portability, and security.

A `docker-compose.yml` file was also created as the orchestrator of the full three-tier stack. This means that the orchestrator defines what should be done and in which order. It also defines which parts of the orchestration are dependant on other services to correctly control the application deployment process.

Orchestration also automates manual tasks such as defining networks, connectivity between containers, port mappings, environment variables, and persistent storage volumes.

With orchestration these values and dependencies can be defined inside a single YAML file that, when executed, automatically builds and deploys the environment in the correct order. In this scenario the orchestrator built the frontend and backend images, created the containers for the three tiers of the application, configured the internal Docker network, and linked the services successfully.

Another important concept implemented during this deployment was idempotency. Because the infrastructure and deployment logic are defined as code inside the Dockerfiles and Compose configuration, the same deployment process can be executed multiple times while consistently recreating the same expected environment and service structure. This reduces configuration drift and improves reproducibility across deployments.

**Decisions I made and why:**

Changed the database image from:
`postgres:18-alpine`
to:
`postgres:16-alpine`

**What went wrong/How I fixed it:**

This change was a strategic decision whose intent was to avoid compatibility and volume mounting issues introduced within PostgreSQL 18 containers during deployment. The PostgreSQL 18 image expected a different internal data storage structure which caused continuous container restart loops and prevented the database service from starting correctly.

Using `postgres:16-alpine` provided a more stable and compatible deployment environment for this lab scenario while still maintaining a lightweight Alpine-based image.

**Thoughts/Considerations:**

Using an orchestrator improves automation by making the application deployment more idempotent, as the order in which the installation, configuration, networking, and application startup occur is already defined inside the YAML file.

This ensures that the same deployment process can be repeated consistently while reducing manual configuration drift and deployment inconsistencies. It also helps prevent mismatches such as networking and dependency issues because the services, ports, connectivity, and startup order are centrally controlled and automatically managed by the orchestrator.

[WEEK 3]

**What I built**

Installed a local cluster development environment using Minikube and used Kubernetes to orchestrate the application deployment.

Minikube was used because of the facilities it provides such as easy local Kubernetes cluster setup and orchestration testing directly on the host machine. Kubectl was used as the main CLI to interact with the Kubernetes environment.

Developed Kubernetes manifest files for each layer of the application, including Deployment and Service manifests. Isolation of these functions into separate files improves troubleshooting, scalability and workload management.

Replicas and self-healing mechanisms were implemented to reduce fatal failures and improve automated recovery. Multiple replicas were created to distribute traffic during peak usage hours with the help of Kubernetes load balancing.

Example:
spec:
  replicas: 3

This ensures Kubernetes continuously maintains the desired number of pod replicas defined in the declarative configuration.

Services were implemented to provide stable networking communication between pods and application layers. This ensures workloads can communicate reliably even if pod IP addresses change during runtime.

**Decisions I made and why:**

Three replicas were used for the frontend and backend deployments while only one replica was used for the database deployment.

The reason for this decision was to distribute traffic more efficiently during busy periods and improve availability if one of the frontend or backend pods failed.

The database deployment remained with a single replica because database replication and state management require additional configuration and were outside the current project scope.

**What went wrong/How I fixed it:**

Frontend and backend deployments initially failed with the following Kubernetes error:
ImagePullBackOff

This issue occurred because Kubernetes attempted to pull the images from an external registry instead of using the local Docker images already built inside the development environment.

To troubleshoot the issue the following configuration was added to the Deployment manifests:

spec:
  containers:
  - name: frontend
    image: frontend-image
    imagePullPolicy: IfNotPresent

The line:
imagePullPolicy: IfNotPresent

forces Kubernetes to use the local image if it already exists instead of always attempting to pull it from an external registry.

**Thoughts/Considerations:**

When deploying a multi-tier cloud-native application it is important to assume failures and unexpected conditions will occur. Because of this the infrastructure should always be designed with resilience, scalability, automation and recovery mechanisms in mind to reduce downtime and improve reliability.