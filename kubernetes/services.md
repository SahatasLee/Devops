# Service

## ClusterIP

## NodePort

## LoadBalancer

## ExternalName

## Ingress


apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  labels:
    app: nginx
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 80
    protocol: TCP
  selector:
    app: nginx

apiVersion: v1
kind: Pod
metadata:
  annotations:
    cni.projectcalico.org/containerID: 2317eacf25d7883befa41bc95255e47952165f2f3ba98986074569cce9e61396
    cni.projectcalico.org/podIP: 10.233.90.5/32
    cni.projectcalico.org/podIPs: 10.233.90.5/32
  creationTimestamp: "2023-10-20T04:33:59Z"
  generateName: nginx-deployment-ff6655784-
  labels:
    app: nginx
    pod-template-hash: ff6655784
  name: nginx-deployment-ff6655784-6r7zm
  namespace: default
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: ReplicaSet
    name: nginx-deployment-ff6655784
    uid: 5acae67f-3d6a-40ba-9f5e-49c5f7394e05
  resourceVersion: "344620"
  uid: 9f90c075-d0e5-4ff1-aaf7-cf536dcdb609
spec:
  containers:
  - image: nginx:1.16.1
    imagePullPolicy: IfNotPresent
    name: nginx
    name: nginx
    ports:
    - containerPort: 80
      protocol: TCP
    resources: {}
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-cwbgn
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  nodeName: node1
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: Always
  schedulerName: default-scheduler
  securityContext: {}
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 30
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  volumes:
  - name: kube-api-access-cwbgn
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2023-10-20T04:33:59Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2023-10-20T04:34:17Z"
    status: "True"
    type: Ready

kubectl expose deployment nginx --port=80 --type=LoadBalancer