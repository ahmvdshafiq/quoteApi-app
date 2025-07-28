variable "subscription_id" {
  description = "The subscription ID for the Azure account"
  type        = string
  sensitive   = true
}

variable "location" {
  default = "eastus"
}

variable "resource_group_name" {
  default = "quoteapp-rg"
}

variable "aks_cluster_name" {
  default = "quote-aks-cluster"
}

variable "acr_name" {
  default = "quoteacrregistry"
}
