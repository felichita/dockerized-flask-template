[deploy kubernetes(namespace: default)]
ansible-playbook -i hosts -D site.yaml -l k8s-primary

