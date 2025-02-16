# Web App Role

This Ansible role deploys a Docker-based web application using Docker Compose. It includes tasks for setting up Docker, deploying the application, and optionally wiping the Docker container and related files.

---

## Requirements

- **Ansible**: Version 2.9 or higher.
- **Docker**: The target host must support Docker installation.
- **Python**: Python 3.x is required on the target host.

---

## Role Variables

The following variables are used in this role. They can be defined in `defaults/main.yml`, `vars/main.yml`, or passed via the playbook.

| Variable Name         | Default Value                  | Description                                                               |
| --------------------- | ------------------------------ | ------------------------------------------------------------------------- |
| `docker_image_name` | `spaghettic0der/moscow-time` | Name of the Docker image to deploy.                                       |
| `docker_image_tag`  | `latest`                     | Tag of the Docker image to deploy.                                        |
| `app_port`          | `8000`                       | Port on which the application runs inside the container.                  |
| `wipe_image`        | `false`                      | Whether to perform a full wipe of the Docker container and related files. |

---

## Tasks Overview

### **1. Deploy Application**

- Pulls the Docker image.
- Creates the application directory (`/opt/web_app`).
- Deploys the Docker Compose file using a Jinja2 template.
- Starts the application using Docker Compose.
- Tags: `deploy`, `docker`

### **2. Wipe Docker Container and Files**

- Stops and removes the Docker container.
- Deletes the Docker Compose file.
- Removes the Docker image.
- Tag: `wipe`
- Controlled by the `wipe_image` variable.

---

## Usage

### **1. Include the Role in Your Playbook**

Add the `web_app` role to your playbook:

```yaml
- hosts: all
  become: yes
  vars:
    docker_image_name: "spaghettic0der/moscow-time"
    docker_image_tag: "latest"
    app_port: 8000
    wipe_image: false
  roles:
    - role: web_app
```

### **2. Run the Playbook**

Execute the playbook:

```
ansible-playbook -i inventory playbook.yml
```

## Docker Compose Template

The role uses a Jinja2 template (templates/docker-compose.yml.j2) to generate the Docker Compose file dynamically. Here's the template:

```
version: '3'
services:
  app:
    image: "{{ docker_image_name }}:{{ docker_image_tag }}"
    container_name: "{{ container_name }}"
    ports:
      - "{{ app_port }}:8000"
    restart: always
```

## Wipe Logic

The wipe logic is defined in tasks/0-wipe.yml and can be enabled by setting wipe_image: true. It performs the following tasks:

Stops and removes the Docker container.

Deletes the Docker Compose file.

Detect the image ID.

Removes the Docker image using the image ID.

To run the wipe tasks independently:

- set the wipe_image to `true` and run:

```
ansible-playbook -i inventory playbook.yml --tags wipe
```
