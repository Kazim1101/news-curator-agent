#!/usr/bin/env python3
"""
Script to run the Streamlit app for the news curator agent.
"""

import subprocess
import sys
import os

def main():
    # Change to the agent directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Run streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.port", "8501",
            "--server.headless", "true"
        ], check=True)
    except KeyboardInterrupt:
        print("\nStreamlit app stopped.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()