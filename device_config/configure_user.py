from pathlib import Path
import subprocess

PROJECT ROOT = Path(__file__).resolve().parents[1]
PLAYBOOK_DIR = PROJECT ROOT / "ansible" / "kwan_user_banner_route"

def main():
    subprocess.run(
        ["ansible-playbook", "configure_user.yaml"],
        cwd=PLAYBOOK_DIR
    )

if __name == "__main__":
    main()
