# Repository Structure

This document outlines the organized structure of the GitHub Dorking repository.

## Overall Structure

```
GitHub Dorking/
├── .github/
│   └── workflows/
│       └── dorking-scan.yml
├── docs/
│   ├── DORK_CATEGORIES_EXPLAINED.md
│   ├── GITHUB_DORKING_GUIDE.md
│   ├── README.md
│   ├── RESPONSIBLE_DORKING.md
│   ├── TOP_DORKS.md
│   └── USAGE.md
├── scripts/
│   ├── README.md
│   ├── dorking_helper.bat
│   ├── dorking_helper.py
│   └── dorking_helper.sh
├── .gitignore
├── CATEGORIES.md
├── CONTRIBUTING.md
├── GitHub Dorking.txt
├── LICENSE
└── README.md
```

## Directory Breakdown

### Root Directory
Contains essential project files:
- `GitHub Dorking.txt` - The main file with all dorking patterns
- `README.md` - Main project documentation with repository organization
- `LICENSE` - MIT License
- `.gitignore` - Git ignore rules
- `CONTRIBUTING.md` - Contribution guidelines
- `CATEGORIES.md` - High-level category descriptions

### docs/ Directory
Contains comprehensive documentation:
- `GITHUB_DORKING_GUIDE.md` - Complete guide to using GitHub dorks
- `DORK_CATEGORIES_EXPLAINED.md` - Detailed explanations of each category
- `RESPONSIBLE_DORKING.md` - Ethical usage guidelines
- `TOP_DORKS.md` - Most effective dorking patterns
- `USAGE.md` - Detailed usage instructions
- `README.md` - Documentation directory overview

### scripts/ Directory
Contains helper tools:
- `dorking_helper.py` - Cross-platform Python script
- `dorking_helper.bat` - Windows batch script
- `dorking_helper.sh` - Linux/Mac shell script
- `README.md` - Scripts directory overview

### .github/workflows/ Directory
Contains GitHub Actions workflows:
- `dorking-scan.yml` - Example workflow for automated scanning

## Benefits of This Organization

1. **Clear Separation of Concerns**:
   - Documentation is separate from code
   - Scripts are organized separately
   - Main dorking patterns are easily accessible

2. **Easy Navigation**:
   - Users can find what they need quickly
   - Related files are grouped together
   - README files in each directory provide context

3. **Scalability**:
   - New documentation can be added to docs/
   - New scripts can be added to scripts/
   - Additional workflows can be added to .github/workflows/

4. **Maintainability**:
   - Changes to documentation don't affect code
   - Script updates are isolated
   - Easy to locate and modify specific components

## Usage Patterns

### For Security Researchers
1. Start with `docs/GITHUB_DORKING_GUIDE.md` for an overview
2. Use `docs/DORK_CATEGORIES_EXPLAINED.md` for detailed category information
3. Refer to `docs/TOP_DORKS.md` for the most effective patterns
4. Use scripts in `scripts/` directory for automated workflows

### For Developers
1. Check `scripts/` directory for helper tools
2. Review `docs/USAGE.md` for detailed instructions
3. Follow guidelines in `docs/RESPONSIBLE_DORKING.md` for ethical usage

### For Contributors
1. Follow guidelines in `CONTRIBUTING.md`
2. Add new documentation to `docs/` directory
3. Add new scripts to `scripts/` directory
4. Update relevant README files

This organization makes the repository professional, easy to navigate, and maintainable for all users.