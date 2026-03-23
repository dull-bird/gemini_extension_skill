import os
import shutil
import subprocess
import tempfile

REPO_URL = "https://github.com/google-gemini/gemini-cli.git"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")

def main():
    print(f"Cloning latest documentation from {REPO_URL}...")
    
    # Create a temporary directory to clone the repo into
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            # Use git clone --depth=1 to fetch only the latest commit, minimizing transfer size
            subprocess.run(
                ["git", "clone", "--depth", "1", REPO_URL, temp_dir],
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Failed to clone repository: {e}")
            print("Tip: If you are behind a firewall, ensure git proxy settings are configured.")
            return

        source_docs = os.path.join(temp_dir, "docs")
        
        if not os.path.exists(source_docs):
            print("Could not find 'docs' directory in the cloned repository.")
            return
            
        print(f"Copying files to local '{DOCS_DIR}' directory...")
        # Ensure target directory exists
        os.makedirs(DOCS_DIR, exist_ok=True)
        
        # Copy the docs folder, overwriting existing files
        shutil.copytree(source_docs, DOCS_DIR, dirs_exist_ok=True)

    print("Documentation successfully updated!")

if __name__ == "__main__":
    main()
