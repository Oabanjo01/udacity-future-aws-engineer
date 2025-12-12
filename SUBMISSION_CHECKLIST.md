# Submission Checklist - Intelligent Document Querying System

## Required Files

### 1. Screenshots Folder ✓
Create a `screenshots` folder with the following images:

#### Infrastructure Setup
- [ ] `terraform_apply_stack1_output.png` - Terraform apply output for stack1 (S3, Aurora)
- [ ] `terraform_apply_stack2_output.png` - Terraform apply output for stack2 (Knowledge Base)
- [ ] `aws_s3_bucket.png` - S3 bucket with uploaded PDF files
- [ ] `aws_aurora_database.png` - Aurora PostgreSQL database in AWS Console
- [ ] `aws_bedrock_kb.png` - Bedrock Knowledge Base in AWS Console

#### Database Configuration
- [ ] `pg_extension_query.png` - Query result showing vector extension enabled
- [ ] `bedrock_kb_table.png` - Query result showing bedrock_integration.bedrock_kb table

#### Application Screenshots
- [ ] `streamlit_app_interface.png` - Main Streamlit application interface
- [ ] `query_example_with_sources.png` - Example query showing source information
- [ ] `010-valid-prompt-sample-output.png` - Terminal output showing valid_prompt() filtering

### 2. Code Files ✓
All code files are included in the project:

#### Terraform Configuration
- [ ] `intelligent-document-search/stack1/main.tf` - S3 and Aurora infrastructure
- [ ] `intelligent-document-search/stack1/variables.tf`
- [ ] `intelligent-document-search/stack1/outputs.tf`
- [ ] `intelligent-document-search/stack2/main.tf` - Bedrock Knowledge Base
- [ ] `intelligent-document-search/stack2/variables.tf`
- [ ] `intelligent-document-search/stack2/outputs.tf`
- [ ] `intelligent-document-search/modules/` - Terraform modules

#### Python Application
- [ ] `intelligent-document-search/app.py` - Main Streamlit application
- [ ] `intelligent-document-search/bedrock_utils.py` - Bedrock utility functions
- [ ] `intelligent-document-search/requirements.txt` - Python dependencies

#### Scripts
- [ ] `intelligent-document-search/scripts/upload_s3.py` - S3 upload script
- [ ] `intelligent-document-search/scripts/aurora_sql.sql` - Database setup SQL
- [ ] `intelligent-document-search/scripts/spec-sheets/*.pdf` - Heavy machinery PDFs

#### Demo/Test Files
- [ ] `intelligent-document-search/demo_validation.py` - Validation demonstration
- [ ] `intelligent-document-search/test_valid_prompt.py` - Validation testing

### 3. Documentation ✓
- [ ] `temperature_top_p_explanation.md` (or .pdf/.docx) - Parameter explanation
- [ ] `intelligent-document-search/README.md` - Project documentation
- [ ] `intelligent-document-search/STANDOUT_FEATURES.md` - Standout features guide

## Rubric Requirements

### Infrastructure Setup
- [x] Terraform configuration for S3 bucket
- [x] Terraform configuration for Aurora PostgreSQL with pgvector
- [x] Terraform configuration for Bedrock Knowledge Base
- [x] Successfully deployed infrastructure (screenshots required)

### Database Configuration
- [x] pgvector extension enabled
- [x] bedrock_integration schema created
- [x] bedrock_kb table with vector column
- [x] HNSW index for vector search

### Document Upload
- [x] Python script to upload PDFs to S3
- [x] At least 5 heavy machinery spec sheets uploaded
- [x] Knowledge Base synced with S3 documents

### Application Development
- [x] Streamlit chat interface
- [x] `query_knowledge_base()` function implemented
- [x] LLM response generation with context
- [x] Configurable temperature and top_p parameters

### Documentation
- [x] Clear explanation of temperature and top_p (1-2 paragraphs)
- [x] Code comments and documentation

### Stand Out Features (Optional but Recommended)
- [x] Valid prompt filtering with terminal output demonstration
- [x] Source information display (S3 URIs, relevance scores)
- [x] Enhanced user experience (loading spinners, error handling)
- [x] Comprehensive documentation

## Files to EXCLUDE from Submission

These files are automatically excluded by the submission script:
- `.terraform/` folders (1.5GB of provider plugins - not needed!)
- `venv/` folders (Python virtual environments)
- `__pycache__/` folders (Python cache)
- `.git/` folder (version control)
- `.DS_Store` files (macOS metadata)
- `*.tfstate.backup` files (Terraform backup states)

## Submission Steps

1. **Create Screenshots Folder**
   ```bash
   mkdir -p screenshots
   ```
   Add all required screenshots to this folder.

2. **Run Demo for Screenshot**
   ```bash
   python intelligent-document-search/demo_validation.py
   ```
   Screenshot the terminal output and save as `screenshots/010-valid-prompt-sample-output.png`

3. **Convert Documentation (Optional)**
   If required, convert `temperature_top_p_explanation.md` to PDF:
   - Use an online converter, or
   - Open in a text editor and export as PDF

4. **Prepare Submission Package**
   ```bash
   ./prepare_submission.sh
   ```
   Enter your name when prompted.

5. **Verify Package Contents**
   ```bash
   unzip -l LastName_FirstName_ProjectSubmission.zip | head -50
   ```

6. **Check Package Size**
   Should be under 100MB (without .terraform folders)
   ```bash
   ls -lh LastName_FirstName_ProjectSubmission.zip
   ```

7. **Submit**
   Upload `LastName_FirstName_ProjectSubmission.zip` to the course portal.

## Expected Package Size

- **With .terraform folders**: ~1.6 GB ❌
- **Without .terraform folders**: ~50-100 MB ✅

The `.terraform` folders contain downloaded provider plugins that can be regenerated with `terraform init`. They are NOT needed for submission.

## Final Verification

Before submitting, verify:
- [ ] All screenshots are clear and legible
- [ ] All code files are included
- [ ] Documentation is complete
- [ ] Package size is reasonable (<100MB)
- [ ] File naming follows requirements
- [ ] No sensitive information (AWS keys, passwords) in files

## Questions?

If you encounter any issues:
1. Check that all screenshots are in the `screenshots/` folder
2. Verify the zip file extracts correctly
3. Ensure all rubric requirements are met
4. Review the project README for additional guidance

Good luck with your submission! 🚀
