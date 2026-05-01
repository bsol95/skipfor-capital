import sys
import json
import subprocess

data = json.load(sys.stdin)
fp = data.get('tool_input', {}).get('file_path', '')

if 'skipfor_capital' in fp:
    repo = r'C:\Users\bsolender\skipfor_capital'
    subprocess.run(['git', '-C', repo, 'add', '-A'])
    result = subprocess.run(['git', '-C', repo, 'commit', '-m', 'Update site'], capture_output=True)
    if result.returncode == 0:
        subprocess.run(['git', '-C', repo, 'push'])
