#!/bin/bash

# Submission Preparation Script
# This script creates a clean zip file for project submission

echo "================================================"
echo "Preparing Intelligent Document Querying System"
echo "Project Submission Package"
echo "================================================"
echo ""

# Get student name
read -p "Enter your Last Name: " LASTNAME
read -p "Enter your First Name: " FIRSTNAME

SUBMISSION_NAME="${LASTNAME}_${FIRSTNAME}_ProjectSubmission"
TEMP_DIR="submission_temp"

echo ""
echo "Creating submission package: ${SUBMISSION_NAME}.zip"
echo ""

# Create temporary directory
mkdir -p "$TEMP_DIR"

# Copy project files, excluding unnecessary items
echo "Copying project files..."
rsync -av --progress \
  --exclude='.git' \
  --exclude='venv' \
  --exclude='__pycache__' \
  --exclude='.terraform' \
  --exclude='*.tfstate.backup' \
  --exclude='.DS_Store' \
  --exclude='submission_temp' \
  --exclude='*.zip' \
  --exclude='prepare_submission.sh' \
  . "$TEMP_DIR/"

echo ""
echo "Files copied. Package contents:"
du -sh "$TEMP_DIR"
echo ""

# Create the zip file
echo "Creating zip file..."
cd "$TEMP_DIR"
zip -r "../${SUBMISSION_NAME}.zip" . -x "*.git*" "*.DS_Store"
cd ..

# Cleanup
echo ""
echo "Cleaning up temporary files..."
rm -rf "$TEMP_DIR"

echo ""
echo "================================================"
echo "✅ Submission package created successfully!"
echo "================================================"
echo ""
echo "File: ${SUBMISSION_NAME}.zip"
ls -lh "${SUBMISSION_NAME}.zip"
echo ""
echo "Package size:"
du -h "${SUBMISSION_NAME}.zip"
echo ""
echo "Next steps:"
echo "1. Create 'screenshots' folder and add all required screenshots"
echo "2. Convert temperature_top_p_explanation.md to PDF if needed"
echo "3. Verify all rubric requirements are met"
echo "4. Submit ${SUBMISSION_NAME}.zip to the course portal"
echo ""
