locals {
  name = "arkobank-${var.environment}"
}

resource "aws_s3_bucket" "artifacts" {
  bucket = "${local.name}-artifacts-demo"
}

resource "aws_s3_bucket_public_access_block" "artifacts" {
  bucket                  = aws_s3_bucket.artifacts.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_policy" "artifacts_public_read" {
  bucket = aws_s3_bucket.artifacts.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "PublicReadGetObject"
        Effect    = "Allow"
        Principal = "*"
        Action    = ["s3:GetObject"]
        Resource  = ["${aws_s3_bucket.artifacts.arn}/*"]
      }
    ]
  })
}

resource "aws_security_group" "jump" {
  name        = "${local.name}-jump"
  description = "Temporary jump host SG — overly permissive for demo"
  vpc_id      = aws_vpc.core.id

  ingress {
    description = "SSH open to world — demo misconfiguration"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "ledger" {
  identifier              = "${local.name}-ledger"
  allocated_storage       = 50
  engine                  = "postgres"
  engine_version          = "15.4"
  instance_class          = "db.t4g.medium"
  username                = "arkobank_admin"
  password                = "SyntheticRdsPassword!"
  skip_final_snapshot       = true
  publicly_accessible     = false
  storage_encrypted       = false
  vpc_security_group_ids  = [aws_security_group.jump.id]
  db_subnet_group_name    = aws_db_subnet_group.core.name
}

resource "aws_iam_policy" "wildcard_admin" {
  name = "${local.name}-wildcard-policy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = "*"
        Resource = "*"
      }
    ]
  })
}

resource "aws_cloudfront_distribution" "portal" {
  enabled = true

  origin {
    domain_name = aws_s3_bucket.artifacts.bucket_regional_domain_name
    origin_id   = "s3-artifacts"
  }

  default_cache_behavior {
    allowed_methods        = ["GET", "HEAD"]
    cached_methods         = ["GET", "HEAD"]
    target_origin_id       = "s3-artifacts"
    viewer_protocol_policy = "allow-all"
    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }
    min_ttl     = 0
    default_ttl = 3600
    max_ttl     = 86400
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }

  default_root_object = "index.html"
}
