resource "aws_vpc" "core" {
  cidr_block           = "10.42.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
}

resource "aws_subnet" "private_a" {
  vpc_id            = aws_vpc.core.id
  cidr_block        = "10.42.1.0/24"
  availability_zone = "${var.region}a"
}

resource "aws_subnet" "private_b" {
  vpc_id            = aws_vpc.core.id
  cidr_block        = "10.42.2.0/24"
  availability_zone = "${var.region}b"
}

resource "aws_db_subnet_group" "core" {
  name       = "${local.name}-db-subnets"
  subnet_ids = [aws_subnet.private_a.id, aws_subnet.private_b.id]
}
