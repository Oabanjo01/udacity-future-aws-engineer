# Quick Submission Guide

## TL;DR - Create Your Submission Package

```bash
# 1. Create the validation demo screenshot
python intelligent-document-search/demo_validation.py
# Screenshot the output and save to screenshots/010-valid-prompt-sample-output.png

# 2. Add all other required screenshots to screenshots/ folder

# 3. Create the submission zip (excludes .terraform folders automatically)
python create_submission.py
# Enter your name when prompted

# 4. Submit the zip file!
```

## What Gets Excluded (Automatically)

✅ These large/unnecessary files are automatically excluded:
- `.terraform/` folders (1.5GB of provider plugins)
- `venv/` folders (Python virtual environments)
- `__pycache__/` folders (Python cache)
- `.git/` folder (version control)
- `.DS_Store` files (macOS metadata)
- `*.tfstate.backup` files (Terraform backups)

## What Gets Included

✅ Everything you need for submission:
- All Terraform configuration files (`.tf`)
- All Python code files (`.py`)
- All documentation (`.md`)
- All PDF spec sheets
- Screenshots folder
- Requirements files
- SQL scripts
- Terraform state files (current state only)

## Expected Package Size

- **Before**: ~1.6 GB (with .terraform)
- **After**: ~50-100 MB (without .terraform) ✅

## Required Screenshots

Place these in the `screenshots/` folder:

1. `terraform_apply_stack1_output.png` - Stack1 deployment
2. `terraform_apply_stack2_output.png` - Stack2 deployment
3. `aws_s3_bucket.png` - S3 bucket with PDFs
4. `aws_aurora_database.png` - Aurora database
5. `aws_bedrock_kb.png` - Bedrock Knowledge Base
6. `pg_extension_query.png` - Vector extension enabled
7. `bedrock_kb_table.png` - Database table created
8. `streamlit_app_interface.png` - App interface
9. `query_example_with_sources.png` - Query with sources
10. `010-valid-prompt-sample-output.png` - Validation demo

## Troubleshooting

**Q: Package is still too large?**
A: Run `python create_submission.py` - it automatically excludes large folders

**Q: Missing screenshots?**
A: Create `screenshots/` folder and add all required images

**Q: Need to convert .md to PDF?**
A: Use an online converter or open in a text editor and export as PDF

**Q: Terraform files needed?**
A: Yes, but NOT the `.terraform/` folders - those are auto-excluded

## Final Checklist

- [ ] All 10 screenshots in `screenshots/` folder
- [ ] `temperature_top_p_explanation.md` is complete
- [ ] Ran `python create_submission.py`
- [ ] Zip file is under 200MB
- [ ] Verified key files are in the zip
- [ ] Ready to submit!

## Support

See `SUBMISSION_CHECKLIST.md` for detailed requirements.
