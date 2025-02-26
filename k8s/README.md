# Lab 9:

## Task 1:

- let's create an aws instance and connect to it using ssh:
- ![img](assets/image1.png)
- let's install `minikube` from the official site:
- ![img](assets/image2.png)
- ![img](assets/image3.png)
- let's start a cluster with `docker` driver (at the last line we can see that `kubectl has been configured`)
- ![img](assets/image4.png)
- let's check the `minikube's` status:
- ![img](assets/image5.png)
- let's add `kubectl` and check it:
- ![img](assets/image6.png)
- let's deploy our app_python:
- ![img](assets/image7.png)
- let's create a service to expose our application on port 9100:
- ![img](assets/image8.png)
- let's execute `kubectl get pods,svc`
- ![img](assets/image9.png)
- let's clean up:
  - delete the deployment:
  - ![img](assets/image10.png)
  - delete the service:
  - ![](assets/image11.png)

## Task 2:

- let's create `deployment.yml` file:
- ![img](assets/image12.png)
- let's create `service.yml` file:
- ![img](assets/image13.png)
- let's apply both the deployment and the service:
- ![img](assets/image14.png)
- let's execute `minikube kubectl -- get pods`, `minikube kubectl -- get svc`
- ![img](assets/image15.png)
- let's execute `minikube service --all`
- ![img](assets/image16.png)
- now since i'm using an aws instance, and a docker driver for minikube, i can only access the url of the service internally:
- ![img](assets/image17.png)
- to access the service externally on my local machine, some extra steps should be followed: (it took long time to figure it out :/ )

  - first let's make a port-forward to direct requests going to 32699 to 9100
  - ![img](assets/image29.png)
  - then let's ssh to the instance and let requests to port 32699 be available on my localhost port 32700
  - ![img](assets/image18.png)
  - now let's check the magic and navigate to localhost:32700 on the browser:
  - ![img](assets/image19.png)
  - ![](assets/image20.png)

## Bonus:

- let's create the `deployment.yml` file:
- ![img](assets/image21.png)
- let's create the `service.yml` file:
- ![img](assets/image22.png)
- let's create the `ingress.yml` file:
- ![img](assets/image23.png)
- let's enable ingress addon:
- ![img](assets/image24.png)
- let's apply the files:
- ![img](assets/image25.png)
- let's get the ingress IP and push it to the hosts file:
- ![img](assets/image26.png)
- and finally let's curl to check:
- ![img](assets/image27.png)
- everything is working fine! a final check to the cluster:
- ![](assets/image28.png)
