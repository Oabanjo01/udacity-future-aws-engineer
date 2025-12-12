#!/usr/bin/env python3
"""
Create submission package for Intelligent Document Querying System
Excludes large unnecessary files like .terraform folders
"""

import os
import zipfile
from pathlib import Path

# Files and folders to exclude
EXCLUDE_PATTERNS = [
    '.terraform',
    'venv',
    '__pycache__',
    '.git',
    '.DS_Store',
    '*.pyc',
    '*.tfstate.backup',
    'submission_temp',
    '*.zip',
    'create_submission.py',
    'prepare_submission.sh',
]

# Extra documentation files to exclude (not required for submission)
EXCLUDE_FILES = [
    'SUBMISSION_CHECKLIST.md',
    'QUICK_SUBMISSION_GUIDE.md',
    'README_SUBMISSION.md',
    'screenshots/README.md',
    'temperature_top_p_explanation.md',  # Exclude .md, keep .pdf
    'convert_to_pdf.py',
]

def should_exclude(path):
    """Check if a path should be excluded"""
    path_str = str(path)
    
    # Check against patterns
    for pattern in EXCLUDE_PATTERNS:
        if pattern in path_str:
            return True
    
    # Check against specific files
    for exclude_file in EXCLUDE_FILES:
        if path_str.endswith(exclude_file) or path_str.endswith('./' + exclude_file):
            return True
    
    return False

def create_submission_zip(lastname, firstname):
    """Create submission zip file"""
    zip_name = f"{lastname}_{firstname}_ProjectSubmission.zip"
    
    print("=" * 60)
    print("Creating Submission Package")
    print("=" * 60)
    print(f"\nOutput file: {zip_name}\n")
    
    file_count = 0
    total_size = 0
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through all files
        for root, dirs, files in os.walk('.'):
            # Remove excluded directories from dirs list (modifies in-place)
            dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d))]
            
            for file in files:
                file_path = os.path.join(root, file)
                
                # Skip excluded files
                if should_exclude(file_path):
                    continue
                
                # Add to zip
                arcname = file_path[2:]  # Remove './' prefix
                try:
                    zipf.write(file_path, arcname)
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                    file_count += 1
                    
                    if file_count % 10 == 0:
                        print(f"Added {file_count} files... ({total_size / 1024 / 1024:.1f} MB)")
                except Exception as e:
                    print(f"Warning: Could not add {file_path}: {e}")
    
    zip_size = os.path.getsize(zip_name)
    
    print("\n" + "=" * 60)
    print("✅ Submission package created successfully!")
    print("=" * 60)
    print(f"\nFile: {zip_name}")
    print(f"Files included: {file_count}")
    print(f"Uncompressed size: {total_size / 1024 / 1024:.1f} MB")
    print(f"Compressed size: {zip_size / 1024 / 1024:.1f} MB")
    print(f"Compression ratio: {(1 - zip_size/total_size)*100:.1f}%")
    
    print("\n" + "=" * 60)
    print("Next Steps:")
    print("=" * 60)
    print("1. Add all required screenshots to 'screenshots/' folder")
    print("2. Verify temperature_top_p_explanation.md is complete")
    print("3. Review SUBMISSION_CHECKLIST.md")
    print(f"4. Submit {zip_name} to the course portal")
    print()
    
    return zip_name

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Intelligent Document Querying System")
    print("Submission Package Creator")
    print("=" * 60 + "\n")
    
    lastname = input("Enter your Last Name: ").strip()
    firstname = input("Enter your First Name: ").strip()
    
    if not lastname or not firstname:
        print("\nError: Both first and last name are required!")
        exit(1)
    
    print()
    zip_name = create_submission_zip(lastname, firstname)
    
    # Verify the zip
    print("\nVerifying package contents...")
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        files = zipf.namelist()
        
        # Check for key files
        key_files = [
            'intelligent-document-search/app.py',
            'intelligent-document-search/bedrock_utils.py',
            'intelligent-document-search/stack1/main.tf',
            'intelligent-document-search/stack2/main.tf',
            'temperature_top_p_explanation.pdf',
        ]
        
        print("\nKey files check:")
        for key_file in key_files:
            if key_file in files:
                print(f"  ✅ {key_file}")
            else:
                print(f"  ❌ {key_file} - MISSING!")
        
        # Check for .terraform (should NOT be present)
        terraform_files = [f for f in files if '.terraform' in f]
        if terraform_files:
            print(f"\n  ⚠️  Warning: Found {len(terraform_files)} .terraform files (should be excluded)")
        else:
            print("\n  ✅ No .terraform files (good!)")
    
    print("\n✅ Package ready for submission!\n")
