import re,json,pathlib
base=pathlib.Path(__file__).parent
src=base.parent/'svg-originals'/'lucide-icons'/'icons'
t=(base/'template.html').read_text()
names=set(re.findall(r'\{\{icon:([\w-]+)\}\}',t))|set(re.findall(r"ic\('([\w-]+)'\)",t))|set(re.findall(r"\['\w+','([\w-]+)','",t))|{'circle-check','lock','plus','trash-2','lightbulb','chevron-left','chevron-right'}
def inner(n):
    s=(src/f'{n}.svg').read_text()
    return re.sub(r'^.*?<svg[^>]*>|</svg>\s*$','',s,flags=re.S).strip()
icons={n:inner(n) for n in sorted(names) if (src/f'{n}.svg').exists()}
print('missing',[n for n in names if n not in icons])
t=re.sub(r'\{\{icon:([\w-]+)\}\}',lambda m:f'<svg class="i" viewBox="0 0 24 24" aria-hidden="true">{icons[m.group(1)]}</svg>',t)
t=t.replace('{{icons_json}}',json.dumps(icons))
(base/'index.html').write_text(t);print('ok',len(t),sorted(icons))
