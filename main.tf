terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "local_warehouse" {
  image = "postgres:18"
  name  = "local_zoomcamp_warehouse"
  
  ports {
    internal = 5432
    external = 5433  # 5433 avoids conflicting with your active compose database on 5432
  }

  env = [
    "POSTGRES_USER=root",
    "POSTGRES_PASSWORD=root",
    "POSTGRES_DB=ny_taxi_local"
  ]
}
