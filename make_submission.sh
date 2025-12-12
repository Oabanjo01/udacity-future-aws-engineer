#!/bin/bash

# Simple submission package creator
# Excludes .terraform, venv, and other large folders

echo "======================================================"
echo "Creating Submission Package"
echo "======================================================"
echo ""

read -p "Enter your Last Name: " LASTNAME
read -p "Enter your First Name: " FIRSTNAME

ZIP_NAME="${LASTNAME}_${FIRSTNAME}_ProjectSubmission.zip"

echo ""
echo "Creating: $ZIP_NAME"
echo ""

# Create zip excluding large folders
zip -r "$ZIP_NAME" . \
  -x ".git/*" \
  -x "venv/*" \
  -x "__pycache__/*" \
  -x "*/.terraform/*" \
  -x "*.DS_Store" \
  -x "*.pyc" \
  -x "*.tfstate.backup" \
  -x "*.zip" \
  -x "SUBMISSION_CHECKLIST.md" \
  -x "QUICK_SUBMISSION_GUIDE.md" \
  -x "README_SUBMISSION.md" \
  -x "screenshots/README.md" \
  -x "screenshots/validation_output.txt" \
  -x "temperature_top_p_explanation.md" \
  -x "convert_to_pdf.py" \
  -x "create_submission.py" \
  -x "make_submission.sh" \
  -x "prepare_submission.sh" \
  -x "FINAL_STEPS.txt" \
  -x "aws-bedrock-project/*"

echo ""
echo "======================================================"
echo "✅ Package created!"
echo "======================================================"
echo ""
ls -lh "$ZIP_NAME"
echo ""

# Test the zip
echo "Checking for .terraform folders (should be 0)..."
TERRAFORM_COUNT=$(unzip -l "$ZIP_NAME" | grep -c ".terraform/" || true)
echo "Found: $TERRAFORM_COUNT .terraform folder files"

if [ "$TERRAFORM_COUNT" -gt 0 ]; then
    echo "⚠️  WARNING: .terraform folder files found in zip!"
else
    echo "✅ Good! No .terraform folder files"
fi

echo ""
echo "Verifying key files are included..."
unzip -l "$ZIP_NAME" | grep -q "intelligent-document-search/app.py" && echo "✅ app.py" || echo "❌ app.py MISSING"
unzip -l "$ZIP_NAME" | grep -q "intelligent-document-search/bedrock_utils.py" && echo "✅ bedrock_utils.py" || echo "❌ bedrock_utils.py MISSING"
unzip -l "$ZIP_NAME" | grep -q "temperature_top_p_explanation.pdf" && echo "✅ temperature_top_p_explanation.pdf" || echo "❌ temperature_top_p_explanation.pdf MISSING"

echo ""
echo "Package size:"
du -h "$ZIP_NAME"
echo ""
echo "Ready to submit!"
