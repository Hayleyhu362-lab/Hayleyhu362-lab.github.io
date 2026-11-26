"""Usage: python prepare_social.py https://your-site.example/  (before upload)."""
from pathlib import Path
import sys,re,html
from urllib.parse import urlparse
if len(sys.argv)!=2 or urlparse(sys.argv[1]).scheme!='https' or not urlparse(sys.argv[1]).netloc:raise SystemExit('Supply the final public HTTPS site URL.')
root=Path(__file__).parent; base=sys.argv[1].rstrip('/')+'/'
for path in root.rglob('*.html'):
    s=path.read_text(); url=base+path.relative_to(root).as_posix(); img=base+'assets/social-card.png'
    s=re.sub(r'<meta property="og:(url|image)"[^>]*>','',s);s=s.replace('</head>',f'<meta property="og:url" content="{html.escape(url)}"><meta property="og:image" content="{html.escape(img)}"></head>');path.write_text(s)
print('Absolute social preview URLs configured.')
