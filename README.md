<p align="center">
  <img alt="python-rabbitmq" src="https://habrastorage.org/webt/wj/xp/kf/wjxpkfeg45pxv_pbpaiyykpj9jg.png" width="250px" float="center"/>
</p>

<h1 align="center">Welcome to RabbitMQ Hello Repository</h1>

<p align="center">
  <strong>Python script to send messages to RabbitMQ</strong>
</p>

<p align="center">
  <a href="https://github.com/lpmatos/rabbitmq-hello">
    <img alt="Open Source" src="https://badges.frapsoft.com/os/v1/open-source.svg?v=102">
  </a>

  <a href="https://github.com/lpmatos/rabbitmq-hello/graphs/contributors">
    <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/lpmatos/rabbitmq-hello">
  </a>

  <a href="https://github.com/lpmatos/rabbitmq-hello">
    <img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/lpmatos/rabbitmq-hello">
  </a>

  <a href="https://github.com/lpmatos/rabbitmq-hello">
    <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/lpmatos/rabbitmq-hello">
  </a>

  <a href="https://github.com/lpmatos/rabbitmq-hello/stargazers">
    <img alt="GitHub Stars" src="https://img.shields.io/github/stars/lpmatos/rabbitmq-hello?style=social">
  </a>

  <a href="https://github.com/lpmatos/rabbitmq-hello/commits/master">
    <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/lpmatos/rabbitmq-hello">
  </a>

  <a href="https://github.com/lpmatos/rabbitmq-hello">
    <img alt="Repository Size" src="https://img.shields.io/github/repo-size/lpmatos/rabbitmq-hello">
  </a>

  <a href="https://github.com/lpmatos/rabbitmq-hello/issues">
    <img alt="Repository Issues" src="https://img.shields.io/github/issues/lpmatos/rabbitmq-hello">
  </a>

  <a href="https://github.com/lpmatos/rabbitmq-hello/blob/master/LICENSE">
    <img alt="MIT License" src="https://img.shields.io/github/license/lpmatos/rabbitmq-hello">
  </a>
</p>

### Menu

<p align="left">
  <a href="#pre-requisites">Pre-Requisites</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#about">About</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#description">Description</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#how-to-contribute">How to contribute</a>
</p>

### By me a coffe

Pull requests are welcome. If you'd like to support the work and buy me a ☕, I greatly appreciate it!

<a href="https://www.buymeacoffee.com/EatdMck" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 100px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

### Getting Started

To use this repository you need a **git clone**:

```bash
git clone --depth 1 https://github.com/lpmatos/rabbitmq-hello.git -b master
```

This will give access of the project on your local machine.

### Pre Requisites

To this project you yeed:

* Python 3.8.
* Docker and Docker Compose.
* RabbitMQ.

### Built with

- [Python](https://www.python.org/)
- [RabbitMQ](https://www.rabbitmq.com/documentation.html)
- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### How to use it?

1. Set the gitlab environment variables.
2. Install python packages in requirements.txt.
2. Run this script with docker-compose, Dockerfile or into your local machine with Python command.
3. Profit.

Press CTRL + C to stop it in Docker Compose or Dockerfile.

### Description

Send messages to RabbitQM using Python.

### Running pip

The **pip** is a command line program. When you install **pip**, a **pip** command is added to your system, which can be run from the command prompt as follows:

```bash
$ pip <pip arguments>
```

If you cannot run the pip command directly (possibly because the location where it was installed isn't on your operating systems **PATH**) then you can run **pip** via the **Python** interpreter:

```bash
$ python -m pip <pip arguments>
```

On **Windows**, the py launcher can be used:

```bash
$ py -m pip <pip arguments>
```

### Installing Packages

#### Pip

The **pip** supports installing from **PyPI**, version control, local projects, and directly from distribution files.

The most common scenario is to install from **PyPI** using Requirement specifiers.

```bash
$ pip install SomePackage            # latest version
$ pip install SomePackage==1.0.4     # specific version
$ pip install somePackage>=1.0.4     # minimum version
```

#### Pipenv

**Pipenv** is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the **Python** world. **Windows** is a firsts-class citizen, in our world.

It automatically creates and manages a **virtualenv** for your projects, as well as adds/removes packages from your **Pipfile** as you install/uninstall packages. It also generates the ever-important **Pipfile.lock**, which is used to produce deterministic builds.

##### Installation

```bash
$ pip install pipenv
```

##### Create a TOML Spec Pipfile

You can build the **Pipfile** to specifying:

* Versions of a Package.
* Versions of **Python**.
* Basic configurations.

##### Pipenv Workflow

Clone/create project repository:

```bash
$ cd myproject
```

Install from **Pipfile**, if there is one:

```bash
$ pipenv install
```

Install from **Pipfile** dev:

```bash
$ pipenv install --dev
```

### Requirement File

**Requirement File** are files containing a list of items to be installed using **pip** install like so:

```bash
$ pip install -r requirements.txt
```

Logically, a **Requirement File** is just a list of **pip** install arguments placed in a file. Note that you should not rely on the items in the file being installed by **pip** in any particular order.

### Environment variables

**Name**  |  **Description**
:---:  |  :---:
**RABBITMQ_DEFAULT_USER**  |  Default RabbitMQ User Login
**RABBITMQ_DEFAULT_PASS**  |  Default RabbitMQ User Password

### 🐋 Development with Docker

Steps to build the Docker Image.

#### Build

```bash
docker image build -t <IMAGE_NAME> -f <PATH_DOCKERFILE> <PATH_CONTEXT_DOCKERFILE>
docker image build -t <IMAGE_NAME> . (This context)
```

#### Run

Steps to run the Docker Container.

* **Linux** running:

```bash
docker container run -d -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME> <COMMAND>
docker container run -it --rm --name <CONTAINER_NAME> -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME> <COMMAND>
```

* **Windows** running:

```
winpty docker.exe container run -it --rm <IMAGE_NAME> <COMMAND>
```

For more information, access the [Docker](https://docs.docker.com/) documentation or [this](docs/annotations/docker.md).

### 🐋 Development with Docker Compose

Build and run a docker-compose.

```bash
docker-compose up --build
```

Down all services deployed by docker-compose.

```bash
docker-compose down
```

Down all services and delete all images.

```bash
docker-compose down --rmi all
```

### How to contribute

>
> 1. Make a **Fork**.
> 2. Follow the project organization.
> 3. Add the file to the appropriate level folder - If the folder does not exist, create according to the standard.
> 4. Make the **Commit**.
> 5. Open a **Pull Request**.
> 6. Wait for your pull request to be accepted.. 🚀
>
Remember: There is no bad code, there are different views/versions of solving the same problem. 😊

### Add to git and push

You must send the project to your GitHub after the modifications

```bash
git add -f .
git commit -m "Added - Fixing somethings"
git push origin master
```

### Versioning

- [CHANGELOG](CHANGELOG.md)

### License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

### Author

👤 **Lucca Pessoa**

Hey!! If you like this project or if you find some bugs feel free to contact me in my channels:

> * Email: luccapsm@gmail.com
> * Website: https://github.com/lpmatos
> * Github: [@lpmatos](https://github.com/lpmatos)
> * LinkedIn: [@luccapessoa](https://www.linkedin.com/in/lucca-pessoa-4abb71138/)

### Show your support

Give a ⭐️ if this project helped you!

### Project Status

* ✔️ Finish

---

<p align="center">Feito com ❤️ by <strong>Lucca Pessoa :wave:</p>
