# Ansible Deployment Documentation

## Playbook Execution

to run the playbook, use:

```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml
```

after executing the previous line, we get:

```bash
PLAY [Install Docker using Ansible Role] **************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************
ok: [aws_instance]

TASK [docker : Install required packages] *************************************************************************************************
ok: [aws_instance]

TASK [docker : Add Docker GPG key] ********************************************************************************************************
ok: [aws_instance]

TASK [docker : Add Docker repository] *****************************************************************************************************
ok: [aws_instance]

TASK [docker : Install Docker] ************************************************************************************************************
changed: [aws_instance]

TASK [docker : Enable Docker service to start on boot] ************************************************************************************
ok: [aws_instance]

TASK [docker : Install Docker Compose] ****************************************************************************************************
changed: [aws_instance]

TASK [docker : Add user to Docker group] **************************************************************************************************
ok: [aws_instance]

PLAY RECAP ********************************************************************************************************************************
aws_instance               : ok=8    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```


checking inventory details:

```
ansible-inventory -i inventory/default_aws_ec2.yml --list

ansible-inventory -i inventory/default_aws_ec2.yml --graph
```

we get the following output:

```bash
{
    "_meta": {
        "hostvars": {
            "aws_instance": {
                "ansible_host": "ec2-18-234-98-193.compute-1.amazonaws.com",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "/home/ammar/Desktop/devops/ansible/.ssh/VM_Linux.pem",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "aws_instance"
        ]
    }
}

------------------------------------------------------------------------------------

@all:
  |--@ungrouped:
  |  |--aws_instance
```
