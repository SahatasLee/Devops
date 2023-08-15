# Minio

Installation manual

## Prerequisites

- Kubernetes 1.21 or Later
- Git

## Installation

1. Install Krew

    ```Bash
    kubectl krew update
    kubectl krew install minio
    ```

    See the `krew` installation documentation for instructions on installing krew.

2. Install minio

    ```Bash
    kubectl minio version
    kubectl minio init
    kubectl get pods -n minio-operator
    ```

3. Get Token

    ```Bash
    kubectl get secret -n minio-operator
    kubectl describe secret -n minio-operator console-sa-token-xxxx 
    ```

## Ref

[Minio Documentations](https://github.com/minio/operator)
