# PDF to JPG API

A simple, self-hosted REST API for converting PDF documents to JPG images. Built with Python and FastAPI (or Flask), containerized with Docker, and easy to run locally or in production using Docker Compose.

## Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
  - [1. Clone the repo](#1-clone-the-repo)  
  - [2. Build & run with Docker](#2-build--run-with-docker)  
  - [3. Run with Docker Compose](#3-run-with-docker-compose)  
  - [4. Run locally without Docker](#4-run-locally-without-docker)  
- [Usage](#usage)  
  - [Convert a PDF via cURL](#convert-a-pdf-via-curl)  
  - [Convert a PDF via Python](#convert-a-pdf-via-python)  
- [Configuration](#configuration)  
- [API Reference](#api-reference)  
- [Contributing](#contributing)  
- [License](#license)  

## Features

- **Multi-page support**: convert every page of a PDF into separate JPG files.  
- **Custom page ranges**: specify which pages to convert (e.g. `1-3,5`).  
- **High-quality output**: adjustable DPI and image quality.  
- **Zip packaging**: output images are returned as a single ZIP archive.  
- **Lightweight & fast**: built on a minimal Python image, optimized for speed.

## Prerequisites

- [Docker ≥ 20.10](https://docs.docker.com/get-docker/)  
- [Docker Compose ≥ 1.27](https://docs.docker.com/compose/install/) (optional, if you use `docker-compose.yml`)  
- OR Python ≥ 3.8 and `pip`

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/unamedarwin/pdf-to-jpg-api.git
cd pdf-to-jpg-api
