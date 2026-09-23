#!/usr/bin/env python3
"""
Simple HTTP server for Internet Search API Homepage
"""

import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


class QuietHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Simple handler with minimal logging"""
    
    def log_message(self, format, *args):
        """Log to stderr"""
        print(f"[{self.log_date_time_string()}] {format % args}", file=sys.stderr, flush=True)


def main():
    """Start the HTTP server"""
    # Get port from environment
    port = int(os.environ.get('PORT', 8000))
    host = '0.0.0.0'
    
    # Ensure we're in the right directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print(f"🚀 Starting server on {host}:{port}", file=sys.stderr, flush=True)
    print(f"📁 Serving from: {os.getcwd()}", file=sys.stderr, flush=True)
    
    # Check for index.html
    if not Path('index.html').exists():
        print("❌ ERROR: index.html not found!", file=sys.stderr, flush=True)
        sys.exit(1)
    
    # Create and start server
    server_address = (host, port)
    httpd = HTTPServer(server_address, QuietHTTPRequestHandler)
    
    print("✅ Server ready, listening for requests...", file=sys.stderr, flush=True)
    sys.stderr.flush()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n⛔ Server stopped", file=sys.stderr, flush=True)
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr, flush=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
