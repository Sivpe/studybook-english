# -*- coding: utf-8 -*-
"""Draw flat 2D object SVGs for 'My First Camping Trip' unit."""
import io
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
NAVY, INK, WHITE, LINE = '#1C2A4A', '#23262D', '#FFFFFF', '#C9CED8'
GREEN, YELLOW, ORANGE, RED = '#00A84D', '#F5B700', '#EF7C1C', '#D7372B'
BLUE, BROWN, PURPLE, MUD = '#0052A4', '#8D5B4C', '#996CAC', '#795548'

def svg(name, body, vb='0 0 160 100'):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{body}</svg>\n'
    io.open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n').write(s)

os.makedirs(OUT, exist_ok=True)

# 1. Backpack (c01-backpack.svg)
svg('c01-backpack.svg',
    f'<rect x="52" y="24" width="56" height="66" rx="14" fill="{BLUE}" stroke="{LINE}" stroke-width="2"/>'
    f'<path d="M68 24 V16 C68 12 92 12 92 16 V24" fill="none" stroke="{LINE}" stroke-width="3"/>'
    f'<rect x="60" y="44" width="40" height="34" rx="8" fill="{NAVY}" stroke="{LINE}" stroke-width="2"/>'
    f'<rect x="74" y="38" width="12" height="14" rx="3" fill="{YELLOW}"/>'
    f'<line x1="60" y1="58" x2="100" y2="58" stroke="{LINE}" stroke-width="2"/>'
    f'<circle cx="80" cy="58" r="3.5" fill="{WHITE}"/>')

# 2. Fishing rod & fish (c02-fishing.svg)
svg('c02-fishing.svg',
    f'<line x1="28" y1="82" x2="118" y2="18" stroke="{BROWN}" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="36" cy="76" r="6" fill="{LINE}"/>'
    f'<path d="M118 18 Q136 40 128 72" fill="none" stroke="{LINE}" stroke-width="1.8" stroke-dasharray="3,3"/>'
    f'<circle cx="128" cy="62" r="6" fill="{RED}"/>'
    f'<circle cx="128" cy="62" r="3" fill="{WHITE}"/>'
    f'<path d="M128 72 Q130 84 122 84 Q116 84 118 76" fill="none" stroke="{LINE}" stroke-width="2"/>'
    f'<path d="M130 76 Q146 72 152 78 Q144 82 138 86 Z" fill="{YELLOW}" stroke="{LINE}" stroke-width="1.5"/>')

# 3. Night crescent moon (c03-moon.svg)
svg('c03-moon.svg',
    f'<path d="M72 16 A36 36 0 1 0 108 82 A40 40 0 0 1 72 16 Z" fill="{YELLOW}" stroke="{LINE}" stroke-width="2"/>'
    f'<circle cx="118" cy="28" r="3" fill="{YELLOW}"/>'
    f'<circle cx="38" cy="38" r="2.5" fill="{YELLOW}"/>'
    f'<circle cx="128" cy="60" r="2" fill="{YELLOW}"/>'
    f'<path d="M26 78 Q42 70 60 76 Q78 82 96 74" fill="none" stroke="{LINE}" stroke-width="2.5" stroke-linecap="round"/>')

# 4. Steaming hot chocolate mug (c04-chocolate.svg)
svg('c04-chocolate.svg',
    f'<rect x="52" y="36" width="56" height="52" rx="8" fill="{NAVY}" stroke="{LINE}" stroke-width="2"/>'
    f'<path d="M108 46 C124 46 124 74 108 74" fill="none" stroke="{LINE}" stroke-width="4" stroke-linecap="round"/>'
    f'<ellipse cx="80" cy="36" rx="28" ry="8" fill="{BROWN}"/>'
    f'<ellipse cx="80" cy="36" rx="20" ry="5" fill="#5D4037"/>'
    f'<path d="M70 26 Q66 18 72 12" fill="none" stroke="{LINE}" stroke-width="2.5" stroke-linecap="round"/>'
    f'<path d="M82 26 Q78 16 84 10" fill="none" stroke="{LINE}" stroke-width="2.5" stroke-linecap="round"/>'
    f'<path d="M94 26 Q90 18 96 12" fill="none" stroke="{LINE}" stroke-width="2.5" stroke-linecap="round"/>')

# 5. Night stars (c05-stars.svg)
svg('c05-stars.svg',
    f'<polygon points="80,12 86,28 104,30 90,42 94,60 80,50 66,60 70,42 56,30 74,28" fill="{YELLOW}" stroke="{LINE}" stroke-width="2"/>'
    f'<polygon points="36,44 40,54 50,56 42,64 44,74 36,68 28,74 30,64 22,56 32,54" fill="{YELLOW}" stroke="{LINE}" stroke-width="1.5"/>'
    f'<polygon points="124,50 127,58 136,59 130,66 131,74 124,70 117,74 118,66 112,59 121,58" fill="{YELLOW}" stroke="{LINE}" stroke-width="1.5"/>')

# 6. Campfire & marshmallow (c06-campfire.svg)
svg('c06-campfire.svg',
    f'<line x1="34" y1="82" x2="126" y2="68" stroke="{BROWN}" stroke-width="7" stroke-linecap="round"/>'
    f'<line x1="34" y1="68" x2="126" y2="82" stroke="{MUD}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M80 20 Q98 42 98 62 A18 18 0 0 1 62 62 Q62 42 80 20 Z" fill="{RED}"/>'
    f'<path d="M80 32 Q92 48 92 62 A12 12 0 0 1 68 62 Q68 48 80 32 Z" fill="{ORANGE}"/>'
    f'<path d="M80 44 Q86 52 86 62 A6 6 0 0 1 74 62 Q74 52 80 44 Z" fill="{YELLOW}"/>'
    f'<line x1="104" y1="46" x2="148" y2="24" stroke="{BROWN}" stroke-width="2" stroke-linecap="round"/>'
    f'<rect x="114" y="32" width="12" height="14" rx="3" fill="{WHITE}" stroke="{LINE}" stroke-width="1.5" transform="rotate(-26 120 39)"/>')

# 7. Trail of straw and sock (c07-straw.svg)
svg('c07-straw.svg',
    f'<path d="M24 74 L60 68 M40 82 L76 72 M84 76 L118 64 M98 84 L138 72" stroke="{YELLOW}" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M30 62 L48 76 M70 58 L92 78 M110 56 L130 76" stroke="#D4A017" stroke-width="2.5" stroke-linecap="round"/>'
    f'<path d="M68 28 V54 Q68 66 80 66 H96 Q104 66 104 56 Q104 48 92 48 H84 V28 Z" fill="{BLUE}" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="68" y1="36" x2="84" y2="36" stroke="{WHITE}" stroke-width="3"/>'
    f'<line x1="68" y1="42" x2="84" y2="42" stroke="{WHITE}" stroke-width="3"/>')

# 8. Scarecrow head in woods (c08-scarecrow.svg)
svg('c08-scarecrow.svg',
    f'<line x1="80" y1="40" x2="80" y2="92" stroke="{BROWN}" stroke-width="5" stroke-linecap="round"/>'
    f'<line x1="42" y1="64" x2="118" y2="64" stroke="{BROWN}" stroke-width="5" stroke-linecap="round"/>'
    f'<circle cx="80" cy="46" r="22" fill="#E8D5B5" stroke="{LINE}" stroke-width="2"/>'
    f'<polygon points="44,38 116,38 80,10" fill="{BROWN}" stroke="{LINE}" stroke-width="2"/>'
    f'<ellipse cx="80" cy="38" rx="42" ry="7" fill="{BROWN}" stroke="{LINE}" stroke-width="2"/>'
    f'<circle cx="72" cy="46" r="3" fill="{INK}"/>'
    f'<circle cx="88" cy="46" r="3" fill="{INK}"/>'
    f'<path d="M72 56 Q80 60 88 56" fill="none" stroke="{RED}" stroke-width="2" stroke-linecap="round"/>'
    f'<path d="M62 64 L50 72 M100 64 L112 72 M76 70 L70 82 M84 70 L90 82" stroke="{YELLOW}" stroke-width="2.5" stroke-linecap="round"/>')

# 9. Bag with tent poles (c09-bag-poles.svg)
svg('c09-bag-poles.svg',
    f'<rect x="44" y="44" width="82" height="36" rx="10" fill="{GREEN}" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="24" y1="32" x2="90" y2="60" stroke="#78909C" stroke-width="4" stroke-linecap="round"/>'
    f'<line x1="28" y1="26" x2="94" y2="54" stroke="#B0BEC5" stroke-width="4" stroke-linecap="round"/>'
    f'<line x1="32" y1="20" x2="98" y2="48" stroke="#78909C" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M60 44 C60 34 88 34 88 44" fill="none" stroke="{LINE}" stroke-width="3"/>'
    f'<rect x="80" y="44" width="8" height="36" fill="{NAVY}"/>')

# 10. Completed tent (c10-tent.svg)
svg('c10-tent.svg',
    f'<polygon points="80,18 24,80 136,80" fill="{GREEN}" stroke="{LINE}" stroke-width="2"/>'
    f'<polygon points="80,18 80,80 136,80" fill="#008A3E"/>'
    f'<polygon points="80,38 60,80 100,80" fill="{NAVY}"/>'
    f'<line x1="80" y1="18" x2="80" y2="80" stroke="{LINE}" stroke-width="2"/>'
    f'<line x1="24" y1="80" x2="16" y2="86" stroke="{LINE}" stroke-width="2" stroke-linecap="round"/>'
    f'<line x1="136" y1="80" x2="144" y2="86" stroke="{LINE}" stroke-width="2" stroke-linecap="round"/>'
    f'<line x1="80" y1="18" x2="80" y2="10" stroke="{LINE}" stroke-width="2" stroke-linecap="round"/>')

# Explain tiles
svg('x-backpack.svg',
    f'<rect x="52" y="24" width="56" height="64" rx="14" fill="{BLUE}" stroke="{LINE}" stroke-width="2"/>'
    f'<rect x="62" y="44" width="36" height="30" rx="6" fill="{NAVY}" stroke="{LINE}" stroke-width="1.8"/>'
    f'<rect x="74" y="38" width="12" height="12" rx="3" fill="{YELLOW}"/>')

svg('x-moon.svg',
    f'<path d="M68 18 A32 32 0 1 0 102 78 A36 36 0 0 1 68 18 Z" fill="{YELLOW}" stroke="{LINE}" stroke-width="2"/>')

svg('x-campfire.svg',
    f'<line x1="42" y1="80" x2="118" y2="68" stroke="{BROWN}" stroke-width="6" stroke-linecap="round"/>'
    f'<line x1="42" y1="68" x2="118" y2="80" stroke="{MUD}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M80 24 Q96 44 96 62 A16 16 0 0 1 64 62 Q64 44 80 24 Z" fill="{RED}"/>'
    f'<path d="M80 36 Q90 50 90 62 A10 10 0 0 1 70 62 Q70 50 80 36 Z" fill="{YELLOW}"/>')

svg('x-scarecrow.svg',
    f'<circle cx="80" cy="48" r="22" fill="#E8D5B5" stroke="{LINE}" stroke-width="2"/>'
    f'<polygon points="46,40 114,40 80,12" fill="{BROWN}" stroke="{LINE}" stroke-width="2"/>'
    f'<ellipse cx="80" cy="40" rx="38" ry="6" fill="{BROWN}"/>'
    f'<circle cx="72" cy="48" r="3" fill="{INK}"/><circle cx="88" cy="48" r="3" fill="{INK}"/>')

svg('x-tent.svg',
    f'<polygon points="80,20 28,78 132,78" fill="{GREEN}" stroke="{LINE}" stroke-width="2"/>'
    f'<polygon points="80,20 80,78 132,78" fill="#008A3E"/>'
    f'<polygon points="80,42 62,78 98,78" fill="{NAVY}"/>')

print("15 SVGs generated successfully in site/my-first-camping-trip/img")
