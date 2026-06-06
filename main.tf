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
  name  = "var.container_name"
  
  ports {
    internal = 5432
    external = var.external_port  # 5433 avoids conflicting with your active compose database on 5432
  }

  env = [
    "POSTGRES_USER=${var.postgres_user}",
    "POSTGRES_PASSWORD=${var.postgres_password}",
    "POSTGRES_DB=ny_taxi_local"
  ]
}
