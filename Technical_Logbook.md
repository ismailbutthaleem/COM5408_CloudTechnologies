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

**Thoughts/Considerations:**

Staged deployments should be preferred rather than treated as an optional implementation. They should be considered part of operational excellence procedures because they improve efficiency, scalability, and resource optimisation within an organisation or environment while also reducing unnecessary energy and storage consumption.

Another important consideration is that staged deployments separate the build environment from the runtime environment, allowing only the required application files and production dependencies to be included in the final image.