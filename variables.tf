variable "container_name" {
  description = "The name of our local development database"
  type        = string
  default     = "local_zoomcamp_warehouse"
}

variable "postgres_user" {
  description = "The root username for the database"
  type        = string
  default     = "root"
}

variable "postgres_password" {
  description = "The secure password for the database"
  type        = string
  default     = "root"
}

variable "external_port" {
  description = "The port exposed on your local machine to connect via pgAdmin"
  type        = number
  default     = 5433
}