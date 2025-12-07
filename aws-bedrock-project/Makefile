# Just learnt that - .PHONY tells Make that these are "fake targets" - they're commands to run, not actual files to create.
.PHONY: venv install activate freeze clean help 

venv:
	python3 -m venv venv
	@echo "✓ Virtual environment created!"
	@echo "Run 'make install' to install dependencies"

activate:
	@echo "To activate the virtual environment, run:"
	@echo "  source venv/bin/activate"

install:
	pip install -r requirements.txt
	@echo "✓ Dependencies installed!"

freeze:
	pip freeze > requirements.txt
	@echo "✓ requirements.txt updated!"

clean:
	rm -rf venv
	rm -rf __pycache__
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	@echo "✓ Cleaned up!"

setup: venv install
	@echo "✓ Setup complete! Run 'source venv/bin/activate' to activate"

tf-init-1:
	cd stack1 && terraform init

tf-plan-1:
	cd stack1 && terraform plan -var="db_password=$(PASSWORD)"

tf-apply-1:
	cd stack1 && terraform apply -var="db_password=$(PASSWORD)"

upload:
	python scripts/upload_to_s3.py

help:
	@echo "Available commands:"
	@echo "  make venv        - Create virtual environment"
	@echo "  make install     - Install dependencies"
	@echo "  make freeze      - Save current packages to requirements.txt"
	@echo "  make clean       - Remove virtual environment"
	@echo "  make setup       - Create venv and install dependencies"
	@echo "  make tf-init-1   - Initialize Terraform Stack 1"
	@echo "  make tf-plan-1   - Plan Terraform Stack 1 (requires PASSWORD=xxx)"
	@echo "  make tf-apply-1  - Apply Terraform Stack 1 (requires PASSWORD=xxx)"
	@echo "  make upload      - Upload documents to S3"