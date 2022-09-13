# Best practices for Docker:

## General
1. Avoid defining users as numbers, because this may cause collisions in some environments.  
Prefer **letter naming** instead.
2. Be specific with **versions** used in dependencies.
3. Support configuration of the container via **environment variables**.
4. Use consistent, clear, yet simple, and **appropriate naming** for different stages.
5. Add `docker-compose` file to the root of repository, showing the example of usage.
6. Explicitly mark used ports with `EXPOSE` instruction, so that other images (like automated *NGINX* proxy) may take advantage of this.
7. Include **metadata** labels when building an image -- this helps subsequent managing:
    * application version;
    * link to a website;
    * ways to contact the author and maintainer;
    * etc.

## Lightweight and simplicity
1. Keep images **small** and **standalone**.
2. Avoid unnecessary **dependencies**.
3. Use **multi-stage builds**, when applicable. They allow to:
    * significantly reduce the final size of an image;
    * make use of caching for layers and stages;
    * avoid compiling dependencies.
4. Clear space by removing package manager **cache**.
5. Include `.dockerignore` to reduce docker context size.
6. Organize **layers** concisely to leverage build cache:
    * First install dependencies, and then copy the source code.
    * Push up parts of the Dockerfile that are rarely changed to enable layers caching.
7. **Minimize** number of layers by grouping `RUN`, `COPY` and `ADD` instructions.  
Other instructions do not increase the size of a build.
8. Use `COPY` instructions instead of `ADD` wherever possible.
9. Apply a `COPY` operation only to the source folder, leaving unnecessary files away.
10. **Decouple** different applications from each other, so that each container has only one concern, making it easier to scale horizontally and reuse containers.
11. Make use of *linting* tools to detect bad practices and improve overall style.  
For example *hadolint*, written in purely functional Haskell:  
http://github.com/hadolint/hadolint
12. Consider creating your images based on **Alpine Linux**, which provides considerably slim container.

## Security
1. Use **rootless** user account.  
Run a server as a **restricted user**, lowering the privileges of potentially malicious code.  
For this, apply the `USER` instruction to change the default **UID** from 0 to a custom one.  
Avoid defining users as numbers -- prefer letter naming instead.
2. Make executable binaries **owned by root** and **not writable** (i.e. **read-only**).  
This blocks the executing user from modifying existing binaries and scripts, which prevents various attacks.
3. Avoid unnecessary **privileges**.
4. In a multistage build, create an **intermediate container**, from which then copy only the resulting artifacts to the final image.  
This will reduce the number of files and shrink possible attack surface.
5. Perform **regular scans** on images to detect potential vulnerabilities and security issues:
    * *snyk*: http://snyk.io/
    * *aqua trivy*: http://github.com/aquasecurity/trivy
    * *grype*: http://github.com/anchore/grype
    * and others.

## References and further reading
* Official guides from the Docker team:
    * *Intro Guide to Dockerfile Best Practices*:  
    http://docker.com/blog/intro-guide-to-dockerfile-best-practices/
    * *Best practices for writing Dockerfiles*:  
    http://docs.docker.com/develop/develop-images/dockerfile_best-practices/
    * *Docker development best practices*:  
    http://docs.docker.com/develop/dev-best-practices/
    * *Image-building best practices*:  
    http://docs.docker.com/get-started/09_image_best/
* Commonly accepted and appreciated guidelines:
    * *SYSDIG's Top 20 Dockerfile best practices*:  
    http://sysdig.com/blog/dockerfile-best-practices/  
    http://habr.com/ru/company/domclick/blog/546922/ (Russian version)
    * *SNYK's 10 Docker Security Best Practices*:  
    http://snyk.io/blog/10-docker-image-security-best-practices/
    * *AQUASEC's Ultimate Guide to Top 20 Docker Security Best Practices:*  
    http://blog.aquasec.com/docker-security-best-practices
    * *Docker Best Practices for Python Developers*:  
    http://testdriven.io/blog/docker-best-practices/
    * *Top Docker best practices for secure and lightweight Dockerfiles*:  
    http://datree.io/resources/docker-best-practices
* Other popular guidelines:
    * *Docker Best Practices for Data Scientists*:  
    http://towardsdatascience.com/docker-best-practices-for-data-scientists-2ed7f6876dff
    * *Best practices writing a Dockerfile*:  
    http://engineering.bitnami.com/articles/best-practices-writing-a-dockerfile.html
    * *Docker, Best Practices for Developers & What Next?*:  
    http://dev.to/pavanbelagatti/docker-best-practices-for-developers-what-next-1fjk
    * http://gist.github.com/StevenACoffman/41fee08e8782b411a4a26b9700ad7af5
    * and others...