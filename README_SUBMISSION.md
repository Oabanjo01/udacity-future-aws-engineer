# Intelligent Document Querying System - Submission Package

## Project Overview

This project implements an intelligent document querying system using AWS Bedrock, Aurora PostgreSQL with pgvector, and Streamlit. The system allows users to query heavy machinery specifications using natural language.

## Key Features Implemented

### Core Requirements ✅
- **Infrastructure as Code**: Terraform configurations for S3, Aurora PostgreSQL, and Bedrock Knowledge Base
- **Vector Database**: Aurora PostgreSQL with pgvector extension for semantic search
- **Document Storage**: S3 bucket with 5 heavy machinery PDF spec sheets
- **Knowledge Base**: AWS Bedrock Knowledge Base integrated with S3 and Aurora
- **Chat Application**: Streamlit-based interface with configurable LLM parameters
- **Query Function**: `query_knowledge_base()` retrieves relevant documents using vector similarity

### Stand Out Features ✅
- **Prompt Validation**: AI-powered filtering to ensure queries are about heavy machinery
- **Source Attribution**: Displays document sources with S3 URIs and relevance scores
- **Enhanced UX**: Loading spinners, error handling, expandable source views
- **Comprehensive Documentation**: Detailed guides and explanations

## Project Structure

```
.
├── intelligent-document-search/
│   ├── app.py                          # Main Streamlit application
│   ├── bedrock_utils.py                # Bedrock utility functions
│   ├── requirements.txt                # Python dependencies
│   ├── stack1/                         # Terraform: S3 + Aurora
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── stack2/                         # Terraform: Bedrock KB
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── modules/                        # Terraform modules
│   │   ├── bedrock_kb/
│   │   └── database/
│   ├── scripts/
│   │   ├── upload_s3.py               # S3 upload script
│   │   ├── aurora_sql.sql             # Database setup SQL
│   │   └── spec-sheets/               # Heavy machinery PDFs
│   ├── demo_validation.py             # Validation demonstration
│   └── STANDOUT_FEATURES.md           # Feature documentation
├── screenshots/                        # Required screenshots
├── temperature_top_p_explanation.md    # Parameter explanation
├── SUBMISSION_CHECKLIST.md            # Detailed checklist
└── QUICK_SUBMISSION_GUIDE.md          # Quick reference

```

## Technology Stack

- **Cloud Provider**: AWS
- **Infrastructure**: Terraform
- **Database**: Aurora PostgreSQL with pgvector extension
- **AI/ML**: AWS Bedrock (Claude 3 models)
- **Storage**: Amazon S3
- **Frontend**: Streamlit
- **Language**: Python 3.x

## Key Components

### 1. Infrastructure (Terraform)

**Stack 1**: S3 and Aurora PostgreSQL
- S3 bucket for document storage
- Aurora PostgreSQL cluster with pgvector
- VPC, subnets, and security groups
- IAM roles and policies

**Stack 2**: Bedrock Knowledge Base
- Knowledge Base configuration
- Data source linking to S3
- Vector store configuration with Aurora

### 2. Database Schema

```sql
CREATE SCHEMA bedrock_integration;

CREATE TABLE bedrock_integration.bedrock_kb (
    id uuid PRIMARY KEY,
    embedding vector(1536),
    chunks text,
    metadata json
);

CREATE INDEX bedrock_kb_embedding_idx 
ON bedrock_integration.bedrock_kb 
USING hnsw (embedding vector_cosine_ops);
```

### 3. Python Application

**bedrock_utils.py**:
- `query_knowledge_base()`: Retrieves relevant documents from KB
- `generate_response()`: Generates LLM responses with context
- `valid_prompt()`: Validates prompts are about heavy machinery

**app.py**:
- Streamlit chat interface
- Configurable parameters (temperature, top_p)
- Source attribution display
- Error handling and user feedback

## Configuration Parameters

### Temperature (0.0 - 1.0)
Controls response randomness and creativity:
- **Low (0.0-0.3)**: Focused, deterministic, factual
- **Medium (0.4-0.7)**: Balanced creativity and consistency
- **High (0.8-1.0)**: Creative, diverse, exploratory

### Top_P (0.0 - 1.0)
Controls token selection diversity:
- **Low (0.1-0.3)**: Only most confident predictions
- **Medium (0.5-0.8)**: Balanced coherence and variety
- **High (0.9-1.0)**: Maximum diversity

**Recommended for this use case**: Temperature 0.3-0.5, Top_P 0.8-0.9

## How to Use

### Prerequisites
- AWS Account with appropriate permissions
- Terraform installed
- Python 3.x with pip
- AWS CLI configured

### Deployment Steps

1. **Deploy Infrastructure**
   ```bash
   cd intelligent-document-search/stack1
   terraform init
   terraform apply
   
   cd ../stack2
   terraform init
   terraform apply
   ```

2. **Setup Database**
   ```bash
   # Connect to Aurora and run scripts/aurora_sql.sql
   ```

3. **Upload Documents**
   ```bash
   python scripts/upload_s3.py
   ```

4. **Run Application**
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

## Sample Queries

- "What is the lifting capacity of the excavator X950?"
- "Tell me about the bulldozer BD850 specifications"
- "What are the safety features of the mobile crane MC750?"
- "Compare the dump truck DT1000 with the excavator X950"

## Validation Demo

Run the validation demonstration:
```bash
python intelligent-document-search/demo_validation.py
```

This shows how the system filters prompts to ensure they're about heavy machinery.

## Submission Package

### What's Included
- All Terraform configuration files
- All Python source code
- Documentation and guides
- SQL scripts
- PDF spec sheets
- Screenshots folder
- Parameter explanation document

### What's Excluded
- `.terraform/` folders (1.5GB of provider plugins - can be regenerated)
- `venv/` folders (virtual environments)
- `__pycache__/` folders (Python cache)
- `.git/` folder (version control)

### Package Size
- **With .terraform**: ~1.6 GB ❌
- **Without .terraform**: ~50-100 MB ✅

## Creating Submission Package

```bash
python create_submission.py
```

Enter your name when prompted. The script automatically:
- Excludes large unnecessary files
- Creates a properly named zip file
- Verifies package contents
- Shows compression statistics

## Documentation

- **QUICK_SUBMISSION_GUIDE.md**: Fast reference for creating submission
- **SUBMISSION_CHECKLIST.md**: Detailed rubric requirements
- **STANDOUT_FEATURES.md**: Guide to standout features
- **temperature_top_p_explanation.md**: Parameter explanation

## AWS Resources Created

- S3 Bucket: Document storage
- Aurora PostgreSQL Cluster: Vector database
- Bedrock Knowledge Base: Semantic search engine
- IAM Roles: Service permissions
- VPC Resources: Network infrastructure

## Cost Considerations

- Aurora PostgreSQL: Serverless v2 (scales to zero)
- S3: Standard storage for PDFs
- Bedrock: Pay per API call
- Estimated cost: $10-30/month for light usage

## Cleanup

To avoid ongoing charges:
```bash
cd intelligent-document-search/stack2
terraform destroy

cd ../stack1
terraform destroy
```

## Support and Documentation

For detailed information, see:
- Project README files in each directory
- AWS Bedrock documentation
- Terraform AWS provider documentation
- Streamlit documentation

## Author

[Your Name]
Udacity AI Programming with Python Nanodegree
Final Project: Intelligent Document Querying System

## License

See LICENSE file for details.

---

**Note**: This project demonstrates the integration of modern AI technologies (LLMs, vector databases, semantic search) with cloud infrastructure to create a practical document querying system.
