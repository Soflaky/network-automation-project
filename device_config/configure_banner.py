from pathlib import Path
import subprocess

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PLAYBOOK_DIR = PROJECT_ROOT / "ansible" / "kwan_user_banner_route"

def main():
    subprocess.run(
        ["ansible-playbook", "configure_banner.yaml"],
        cwd=PLAYBOOK_DIR
    )

if __name__ == "__main__":
    main()

