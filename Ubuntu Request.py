import requests
import os
import hashlib
import mimetypes
from urllib.parse import urlparse
from pathlib import Path
import time

class UbuntuImageFetcher:
    def __init__(self):
        self.base_dir = "Fetched_Images"
        self.downloaded_hashes = set()
        self.session = requests.Session()
        # Set a respectful User-Agent header
        self.session.headers.update({
            'User-Agent': 'Ubuntu-Image-Fetcher/1.0 (Respectful Community Tool)'
        })
        self._load_existing_hashes()
    
    def _load_existing_hashes(self):
        """Load hashes of existing images to prevent duplicates"""
        if os.path.exists(self.base_dir):
            for filename in os.listdir(self.base_dir):
                filepath = os.path.join(self.base_dir, filename)
                if os.path.isfile(filepath):
                    try:
                        with open(filepath, 'rb') as f:
                            file_hash = hashlib.md5(f.read()).hexdigest()
                            self.downloaded_hashes.add(file_hash)
                    except Exception:
                        continue
    
    def _validate_url(self, url):
        """Basic URL validation"""
        if not url.startswith(('http://', 'https://')):
            return False, "URL must start with http:// or https://"
        
        parsed = urlparse(url)
        if not parsed.netloc:
            return False, "Invalid URL format"
        
        return True, "Valid URL"
    
    def _check_security_headers(self, response):
        """Check important HTTP headers for security considerations"""
        headers = response.headers
        warnings = []
        
        # Check Content-Type
        content_type = headers.get('content-type', '').lower()
        if not content_type.startswith('image/'):
            warnings.append(f"⚠ Content-Type is '{content_type}', not an image type")
        
        # Check Content-Length for reasonable file size (max 50MB)
        content_length = headers.get('content-length')
        if content_length:
            size_mb = int(content_length) / (1024 * 1024)
            if size_mb > 50:
                warnings.append(f"⚠ Large file size: {size_mb:.1f}MB")
        
        # Check for suspicious headers
        if 'content-disposition' in headers:
            disposition = headers['content-disposition']
            if 'attachment' in disposition and 'filename' in disposition:
                warnings.append("⚠ Server suggests downloading as attachment")
        
        return warnings
    
    def _get_safe_filename(self, url, content_type):
        """Generate a safe filename from URL and content type"""
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        # If no filename in URL, generate one
        if not filename or '.' not in filename:
            # Try to get extension from content-type
            extension = mimetypes.guess_extension(content_type.split(';')[0])
            if not extension:
                extension = '.jpg'  # Default fallback
            
            # Use domain name + timestamp for filename
            domain = parsed_url.netloc.replace('www.', '')
            timestamp = int(time.time())
            filename = f"{domain}_{timestamp}{extension}"
        
        # Sanitize filename
        filename = "".join(c for c in filename if c.isalnum() or c in '.-_')
        return filename
    
    def _is_duplicate(self, content):
        """Check if image content is a duplicate"""
        content_hash = hashlib.md5(content).hexdigest()
        if content_hash in self.downloaded_hashes:
            return True
        self.downloaded_hashes.add(content_hash)
        return False
    
    def fetch_image(self, url):
        """Fetch a single image with comprehensive error handling"""
        print(f"\n🔍 Processing: {url}")
        
        # Validate URL
        is_valid, message = self._validate_url(url)
        if not is_valid:
            print(f"✗ Invalid URL: {message}")
            return False
        
        try:
            # Make request with timeout and stream for large files
            print("📡 Connecting...")
            response = self.session.get(url, timeout=30, stream=True)
            response.raise_for_status()
            
            # Check security headers
            warnings = self._check_security_headers(response)
            for warning in warnings:
                print(warning)
            
            # Get content type
            content_type = response.headers.get('content-type', '').lower()
            
            # Verify it's actually an image
            if not content_type.startswith('image/'):
                print(f"✗ Not an image file (Content-Type: {content_type})")
                return False
            
            # Download content
            print("⬇ Downloading content...")
            content = response.content
            
            # Check for duplicates
            if self._is_duplicate(content):
                print("✗ Duplicate image detected - skipping")
                return False
            
            # Create directory if needed
            os.makedirs(self.base_dir, exist_ok=True)
            
            # Generate safe filename
            filename = self._get_safe_filename(url, content_type)
            filepath = os.path.join(self.base_dir, filename)
            
            # Handle filename conflicts
            counter = 1
            original_filepath = filepath
            while os.path.exists(filepath):
                name, ext = os.path.splitext(original_filepath)
                filepath = f"{name}_{counter}{ext}"
                counter += 1
            
            # Save the image
            with open(filepath, 'wb') as f:
                f.write(content)
            
            # Get file size for display
            file_size = len(content) / 1024  # KB
            
            print(f"✓ Successfully fetched: {os.path.basename(filepath)}")
            print(f"✓ Image saved to {filepath}")
            print(f"✓ File size: {file_size:.1f} KB")
            
            return True
            
        except requests.exceptions.Timeout:
            print("✗ Connection timeout - server took too long to respond")
        except requests.exceptions.ConnectionError:
            print("✗ Connection error - unable to reach server")
        except requests.exceptions.HTTPError as e:
            print(f"✗ HTTP error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"✗ Request error: {e}")
        except PermissionError:
            print("✗ Permission denied - cannot write to directory")
        except OSError as e:
            print(f"✗ File system error: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
        
        return False
    
    def fetch_multiple_images(self, urls):
        """Fetch multiple images with progress tracking"""
        if not urls:
            print("No URLs provided")
            return
        
        print(f"🚀 Starting batch download of {len(urls)} images...")
        print("=" * 50)
        
        successful = 0
        failed = 0
        
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] Processing image...")
            
            if self.fetch_image(url.strip()):
                successful += 1
            else:
                failed += 1
            
            # Be respectful - small delay between requests
            if i < len(urls):
                time.sleep(1)
        
        # Summary
        print("\n" + "=" * 50)
        print("📊 BATCH DOWNLOAD SUMMARY")
        print(f"✓ Successful: {successful}")
        print(f"✗ Failed: {failed}")
        print(f"📁 Images saved in: {os.path.abspath(self.base_dir)}")
        
        if successful > 0:
            print("\nConnection strengthened. Community enriched.")

def main():
    print("🐧 Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web")
    print("Built with Ubuntu principles: Community • Respect • Security")
    print("-" * 60)
    
    fetcher = UbuntuImageFetcher()
    
    while True:
        print("\nChoose an option:")
        print("1. Download single image")
        print("2. Download multiple images")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            url = input("\nPlease enter the image URL: ").strip()
            if url:
                fetcher.fetch_image(url)
                if fetcher.fetch_image(url):
                    print("\nConnection strengthened. Community enriched.")
        
        elif choice == '2':
            print("\nEnter image URLs (one per line, empty line to finish):")
            urls = []
            while True:
                url = input().strip()
                if not url:
                    break
                urls.append(url)
            
            if urls:
                fetcher.fetch_multiple_images(urls)
            else:
                print("No URLs entered.")
        
        elif choice == '3':
            print("\nThank you for using Ubuntu Image Fetcher!")
            print("May your downloads be swift and your community strong. 🐧")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
