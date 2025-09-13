# Ubuntu-Requests
Ubuntu Image Fetcher 🐧

A mindful and secure image downloading tool built with Ubuntu principles of community, respect, and security.


📋 Table of Contents
• [Overview](#overview)
• [Features](#features)
• [Installation](#installation)
• [Usage](#usage)
• [Security Features](#security-features)
• [File Structure](#file-structure)
• [Error Handling](#error-handling)
• [Contributing](#contributing)
• [License](#license)


🌟 Overview

Ubuntu Image Fetcher is a Python-based tool designed to download images from the web in a secure, respectful, and efficient manner. Built with the Ubuntu philosophy in mind, it emphasizes community responsibility, security awareness, and user-friendly operation.


✨ Features

Core Functionality
• **Single Image Download**: Download individual images with detailed feedback
• **Batch Download**: Process multiple URLs simultaneously with progress tracking
• **Duplicate Detection**: Prevents downloading identical images using MD5 hashing
• **Smart Filename Generation**: Automatically generates safe filenames from URLs


Security & Safety
• **URL Validation**: Ensures URLs are properly formatted and secure
• **Content-Type Verification**: Confirms files are actually images
• **HTTP Header Analysis**: Checks security-relevant headers
• **File Size Warnings**: Alerts for unusually large files
• **Safe File Handling**: Sanitizes filenames and prevents path traversal


User Experience
• **Interactive Menu System**: Easy-to-use command-line interface
• **Progress Tracking**: Real-time feedback during downloads
• **Comprehensive Error Messages**: Clear explanations when things go wrong
• **Respectful Rate Limiting**: Built-in delays to be considerate to servers


🚀 Installation

Prerequisites
• Python 3.6 or higher
• `requests` library


Setup
1. **Clone or download the script**:
```bash
wget https://your-repo/ubuntu_image_fetcher.py
# or
git clone https://your-repo/ubuntu-image-fetcher.git
cd ubuntu-image-fetcher
```

2. **Install required dependencies**:
```bash
pip install requests
```

3. **Make the script executable** (optional):
```bash
chmod +x ubuntu_image_fetcher.py
```


📖 Usage

Running the Application

python ubuntu_image_fetcher.py


Menu Options

1. Single Image Download

Choose option 1, then enter a single image URL:
https://example.com/image.jpg


2. Batch Download

Choose option 2, then enter multiple URLs (one per line):
https://example.com/image1.jpg
https://example.com/image2.png
https://example.com/image3.gif
[Press Enter on empty line to start download]


Example Session

🐧 Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web
Built with Ubuntu principles: Community • Respect • Security
------------------------------------------------------------

Choose an option:
1. Download single image
2. Download multiple images
3. Exit

Enter your choice (1-3): 1

Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg

🔍 Processing: https://example.com/ubuntu-wallpaper.jpg
📡 Connecting...
⬇ Downloading content...
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg
✓ File size: 245.7 KB

Connection strengthened. Community enriched.


🔒 Security Features

URL Validation
• Ensures URLs use HTTP/HTTPS protocols
• Validates URL structure and format
• Rejects malformed or suspicious URLs


Content Verification
• Verifies `Content-Type` headers indicate image files
• Checks file extensions match content types
• Warns about suspicious server responses


Safe File Handling
• Sanitizes filenames to prevent directory traversal
• Creates secure file paths within designated directory
• Handles filename conflicts automatically


Network Security
• Uses respectful User-Agent identification
• Implements connection timeouts
• Rate limits requests to be server-friendly


📁 File Structure

project-directory/
├── ubuntu_image_fetcher.py    # Main application
├── README.md                  # This file
└── Fetched_Images/           # Created automatically
    ├── image1.jpg
    ├── image2.png
    └── ...


Generated Files
• **Fetched_Images/**: Directory where all downloaded images are stored
• Images are saved with original or generated filenames
• Duplicate filenames get automatic numbering (e.g., `image_1.jpg`, `image_2.jpg`)


🛠 Error Handling

The application handles various error scenarios gracefully:


Network Errors
• **Connection Timeout**: Server takes too long to respond
• **Connection Error**: Unable to reach server
• **HTTP Errors**: 404, 403, 500, etc.


File System Errors
• **Permission Denied**: Cannot write to directory
• **Disk Space**: Insufficient storage space
• **Path Issues**: Invalid file paths


Content Errors
• **Invalid Content**: Non-image files
• **Corrupted Data**: Incomplete downloads
• **Large Files**: Warnings for files over 50MB


Example Error Messages

✗ Connection timeout - server took too long to respond
✗ Not an image file (Content-Type: text/html)
✗ Duplicate image detected - skipping
⚠ Large file size: 75.3MB
⚠ Content-Type is 'application/octet-stream', not an image type


🔧 Configuration

Customizable Settings

You can modify these constants in the code:


# Maximum file size warning threshold (bytes)
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB

# Request timeout (seconds)
TIMEOUT = 30

# Delay between batch requests (seconds)
REQUEST_DELAY = 1

# Output directory
BASE_DIR = "Fetched_Images"


🤝 Contributing

We welcome contributions that align with Ubuntu principles:


How to Contribute
1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes** with clear, commented code
4. **Test thoroughly** with various image types and URLs
5. **Submit a pull request** with detailed description


Contribution Guidelines
• Follow Python PEP 8 style guidelines
• Add appropriate error handling
• Include security considerations
• Write clear documentation
• Test with edge cases


Areas for Improvement
• Support for additional image formats
• GUI interface option
• Image metadata extraction
• Download resume capability
• Configuration file support
• Logging system


📄 License

This project is released under the MIT License, promoting the Ubuntu philosophy of sharing and community collaboration.


MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.


🐛 Troubleshooting

Common Issues

"Module 'requests' not found"

pip install requests


"Permission denied" errors
• Ensure you have write permissions in the current directory
• Try running from your home directory
• On Linux/Mac, check file permissions: `ls -la`


Downloads failing consistently
• Check your internet connection
• Verify URLs are accessible in a web browser
• Some sites may block automated requests


Large memory usage
• The tool loads entire images into memory
• For very large images, ensure sufficient RAM
• Consider downloading large files individually


Getting Help
• Check the error messages - they're designed to be helpful
• Verify URLs work in a web browser first
• Ensure you have proper internet connectivity
• Try with different image URLs to isolate issues


🌍 Ubuntu Philosophy

This tool embodies Ubuntu principles:

• **Community**: Built to be shared and improved by all
• **Respect**: Respectful to servers and users alike  
• **Security**: Security-conscious design and implementation
• **Accessibility**: Easy to use for everyone
• **Transparency**: Open source and well-documented


⸻


**"Connection strengthened. Community enriched."** 🐧


*Built with ❤️ and the Ubuntu spirit of community collaboration.*
