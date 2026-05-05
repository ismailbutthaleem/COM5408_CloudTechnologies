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