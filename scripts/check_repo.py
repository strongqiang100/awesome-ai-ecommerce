"""Offline documentation, workflow-structure and publication-pattern checks.

This conservative heuristic is not a complete privacy or security audit.
"""
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []
markdown = sorted(ROOT.rglob('*.md'))


def anchors(text):
    explicit = set(re.findall(r'<a id="([^"]+)"', text))
    headings = re.findall(r'^#{1,6}\s+(.+)$', text, re.M)
    for heading in headings:
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        explicit.add(slug)
    return explicit


for path in markdown:
    text = path.read_text()
    if len(re.findall(r'^```', text, re.M)) % 2:
        errors.append(f'{path.relative_to(ROOT)}: unbalanced code fence')
    prose = re.sub(r'```.*?```', '', text, flags=re.S)
    for target in re.findall(r'\]\(([^\s)]+)\)', prose):
        if re.match(r'^[a-zA-Z]+:', target):
            continue
        location, _, fragment = unquote(target).partition('#')
        destination = (path.parent / location).resolve() if location else path
        if not destination.is_relative_to(ROOT):
            errors.append(f'{path.relative_to(ROOT)}: link escapes repository')
        elif not destination.is_file():
            errors.append(f'{path.relative_to(ROOT)}: missing {target}')
        elif fragment and fragment not in anchors(destination.read_text()):
            errors.append(f'{path.relative_to(ROOT)}: missing anchor {target}')

cn = (ROOT/'docs/zh-CN/handbook.md').read_text()
en = (ROOT/'docs/en/handbook.md').read_text()
expected = {f'c{i:02d}' for i in range(1, 21)}
for language, text in [('Chinese', cn), ('English', en)]:
    if set(re.findall(r'<a id="(c\d+)"', text)) != expected:
        errors.append(f'{language}: chapter parity failed')
count = len(re.findall(r'[\u4e00-\u9fff]', cn))
if count < 10000:
    errors.append('Chinese handbook is below 10,000 Han characters')

workflow = json.loads((ROOT/'ai-ecommerce-news-workflow.json').read_text())
names = [node['name'] for node in workflow['nodes']]
if len(set(names)) != len(names):
    errors.append('Duplicate workflow node names')
reached = set()
queue = [node['name'] for node in workflow['nodes'] if node['type'].endswith('.manualTrigger')]
while queue:
    name = queue.pop()
    if name in reached:
        continue
    reached.add(name)
    for group in workflow['connections'].get(name, {}).get('main', []):
        for connection in group:
            if connection['node'] not in names:
                errors.append('Workflow target does not exist')
            else:
                queue.append(connection['node'])
if reached != set(names):
    errors.append('Workflow contains unreachable nodes')
if workflow.get('active') is not False:
    errors.append('Demo must be inactive')

# Patterns detect common leaks, not all personal information.
patterns = {
    'private local path': r'/(?:Users|home)/[A-Za-z0-9_.-]+/',
    'private meeting URL': r'https://[^\s)]+\.(?:feishu|larksuite)\.[^\s)]+/(?:minutes|docx|wiki)/',
    'credential-like token': r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{24,})',
    'email address': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
}
for path in ROOT.rglob('*'):
    if not path.is_file() or '.git' in path.parts or '__pycache__' in path.parts:
        continue
    if path.suffix not in ('.md', '.json', '.yml', '.yaml') and path.name != 'LICENSE':
        continue
    text = path.read_text()
    for label, pattern in patterns.items():
        if re.search(pattern, text):
            errors.append(f'{path.relative_to(ROOT)}: potential {label}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(markdown)} Markdown files, 20 matched chapters, {count} Chinese characters, links, workflow graph, publication patterns')
