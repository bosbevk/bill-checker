import json, math
d=json.load(open('adm3.geojson'))
pick={'Swartland','City of Cape Town','Overstrand'}
def polys(g):
    return g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']]
def bbox(fs):
    xs=[p[0] for f in fs for pl in polys(f['geometry']) for r in pl for p in r]
    ys=[p[1] for f in fs for pl in polys(f['geometry']) for r in pl for p in r]
    return min(xs),min(ys),max(xs),max(ys)
sel=[f for f in d['features'] if f['properties']['shapeName'] in pick]
x0,y0,x1,y1=bbox(sel)
pad=0.25; x0-=pad; x1+=pad*1.6; y0-=pad; y1+=pad
k=math.cos(math.radians((y0+y1)/2))
W,H=560,520
s=min(W/((x1-x0)*k),H/(y1-y0))
ox=(W-(x1-x0)*k*s)/2; oy=(H-(y1-y0)*s)/2
def P(p): return ((p[0]-x0)*k*s+ox, (y1-p[1])*s+oy)
def path(f):
    out=[]
    for pl in polys(f['geometry']):
        for r in pl:
            pts=[P(p) for p in r]
            out.append('M'+' L'.join(f'{a:.1f},{b:.1f}' for a,b in pts)+'Z')
    return ' '.join(out)
def near(f):
    a,b,c,e=bbox([f]); return not (c<x0 or a>x1 or e<y0 or b>y1)
others=[f for f in d['features'] if near(f) and f['properties']['shapeName'] not in pick]
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<defs><filter id="g" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="10" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>']
for f in others: svg.append(f'<path d="{path(f)}" fill="#dfe5ea" stroke="#f3f6f8" stroke-width="1.6" stroke-linejoin="round"/>')
fills={'Swartland':'#1463c9','City of Cape Town':'#0f1b2d','Overstrand':'#1463c9'}
svg.append('<g>')
for f in sel: svg.append(f'<path d="{path(f)}" fill="{fills[f["properties"]["shapeName"]]}" stroke="#f3f6f8" stroke-width="2.5" stroke-linejoin="round"/>')
svg.append('</g>')
# label anchors: centroid of bbox
labels={}
for f in sel:
    a,b,c,e=bbox([f]); labels[f['properties']['shapeName']]=P(((a+c)/2,(b+e)/2))
print(json.dumps(labels))
svg.append('</svg>')
open('map-light.svg','w').write('\n'.join(svg))
