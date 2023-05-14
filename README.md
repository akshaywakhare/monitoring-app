# Monitoring App
--- 
#### Local RUN 
* pip3 install -r requirements.txt
* python3 app.py
* connect to http://localhost:5000 to view the device metrics

#### Docker RUN
* docker build -t <image_name> Dockerfile .
* docker run -p 5000:5000 <image_name>

#### Deploying to MiniKube
* minikube start
* kubectl apply -f deployment.yaml
* connect to http://localhost:5000 to view the device metrics

#### Deploying to Kubernetes
* Login to kubernetes cloud provider
* docker tag <image_name:version> <registry_url/image_name:version>
* docker push <registry_url/image_name:version>
* Update the image url in deployment file under spec->template->spec->container->image
* Check the kubernetes context
   > kubectl config get-context
* kubectl apply -f deployment.yaml
* Check the deployment
   > kubectl get all
* Port forwarding to localhost
   > kubectl port-forward <service_name> 5000:5000