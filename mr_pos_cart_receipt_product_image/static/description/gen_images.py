"""
Generate banner.png (1200x400) and icon.png (128x128)
for the mr_pos_cart_receipt_product_image Odoo module.
Run once:  python gen_images.py
"""
from PIL import Image, ImageDraw, ImageFont
import os, sys

OUTPUT = os.path.dirname(os.path.abspath(__file__))

# ── Palette ──────────────────────────────────────────────────────────────
DARK    = (26,  58,  92)     # #1a3a5c  deep navy
MID     = (25, 118, 210)     # #1976d2  Odoo blue
LIGHT   = (66, 165, 245)     # #42a5f5  sky blue
WHITE   = (255, 255, 255)
ACCENT  = (168, 213, 255)    # light-blue headline tint
DIM     = (160, 200, 240)    # subdued text / icon labels
CARD_BG = (28,  66, 112)     # illustration card fill
CARD_BD = (70, 128, 195)     # illustration card border
ROW1    = (100, 170, 230)    # product row colour 1
ROW2    = ( 90, 190, 180)    # product row colour 2
ROW3    = (210, 120, 160)    # product row colour 3
ROW4    = (180, 130, 210)    # product row colour 4

# ── Helpers ───────────────────────────────────────────────────────────────

def hgradient(draw, w, h, c1, c2, c3=None):
    """Three-stop left-to-right gradient painted as vertical lines."""
    pivot = w // 2 if c3 else w
    for x in range(pivot):
        t = x / max(pivot - 1, 1)
        clr = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
        draw.line([(x, 0), (x, h - 1)], fill=clr)
    if c3:
        for x in range(pivot, w):
            t = (x - pivot) / max(w - pivot - 1, 1)
            clr = tuple(int(c2[i] + (c3[i] - c2[i]) * t) for i in range(3))
            draw.line([(x, 0), (x, h - 1)], fill=clr)


def get_font(size, bold=False):
    candidates = (
        [r"C:\Windows\Fonts\segoeuib.ttf",
         r"C:\Windows\Fonts\arialbd.ttf",
         r"C:\Windows\Fonts\calibrib.ttf"]
        if bold else
        [r"C:\Windows\Fonts\segoeui.ttf",
         r"C:\Windows\Fonts\arial.ttf",
         r"C:\Windows\Fonts\calibri.ttf"]
    )
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def soft_circle(base_img, cx, cy, r, tint=(40, 80, 145), alpha=28):
    """Blend a soft translucent circle onto base_img (RGB)."""
    overlay = Image.new("RGBA", base_img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse([cx - r, cy - r, cx + r, cy + r], fill=tint + (alpha,))
    return Image.alpha_composite(base_img.convert("RGBA"), overlay).convert("RGB")


def rr(draw, x1, y1, x2, y2, r=8, fill=None, outline=None, width=1):
    """rounded_rectangle shorthand."""
    draw.rounded_rectangle([(x1, y1), (x2, y2)],
                            radius=r, fill=fill, outline=outline, width=width)


def text_cx(draw, text, font, cx, y, fill=WHITE):
    """Draw text centred on cx."""
    bb = draw.textbbox((0, 0), text, font=font)
    tw = bb[2] - bb[0]
    draw.text((cx - tw // 2, y), text, font=font, fill=fill)


# ═══════════════════════════════════════════════════════════════
#  BANNER  1200 × 400
# ═══════════════════════════════════════════════════════════════

BW, BH = 1200, 400
banner = Image.new("RGB", (BW, BH))
bd = ImageDraw.Draw(banner)
hgradient(bd, BW, BH, DARK, MID, LIGHT)

# Decorative soft glows
for cx, cy, r in [(1100, 50, 165), (990, 370, 105), (60, 360, 115)]:
    banner = soft_circle(banner, cx, cy, r)
bd = ImageDraw.Draw(banner)

# ── Left-side text ──────────────────────────────────────────────
bd.text((68,  82), "POS Product Image",          font=get_font(52, True), fill=WHITE)
bd.text((68, 148), "on Cart, Receipt & Invoice", font=get_font(44, True), fill=ACCENT)
bd.text((68, 218), "Display product images everywhere a sale happens — in one module.",
        font=get_font(19), fill=DIM)

bd.text((68, 272), "by Mantu Raj",          font=get_font(17, True), fill=(210, 228, 255))
bd.text((68, 300), "workmantu105@gmail.com", font=get_font(15),       fill=DIM)

# ── Right-side illustration cards ───────────────────────────────

def illus_card(d, x, y, w=138, h=135):
    rr(d, x, y, x + w, y + h, r=12, fill=CARD_BG, outline=CARD_BD, width=1)

def product_row(d, ix, iy, iw=48, ih=26, row_color=ROW1, bar_x=None, bw=68):
    """Image thumbnail + two text bars."""
    rr(d, ix, iy, ix + iw, iy + ih, r=5, fill=row_color)
    bx = bar_x if bar_x else ix + iw + 8
    rr(d, bx, iy + 4, bx + bw, iy + 10, r=3, fill=(148, 193, 238))
    rr(d, bx, iy + 14, bx + bw - 18, iy + 18, r=2, fill=(100, 148, 200))


# Card 1 – Cart
illus_card(bd, 702, 55)
product_row(bd, 718, 72, row_color=ROW1, bar_x=778, bw=46)
product_row(bd, 718, 106, row_color=ROW2, bar_x=778, bw=46)
product_row(bd, 718, 140, row_color=ROW3, bar_x=778, bw=46)
text_cx(bd, "POS Cart", get_font(12), 771, 200, DIM)

# Card 2 – Receipt
illus_card(bd, 858, 35, h=165)
product_row(bd, 876, 68,  row_color=ROW1, bar_x=934, bw=52)
product_row(bd, 876, 102, row_color=ROW2, bar_x=934, bw=52)
product_row(bd, 876, 136, row_color=ROW3, bar_x=934, bw=52)
product_row(bd, 876, 170, row_color=ROW4, bar_x=934, bw=52)
text_cx(bd, "Receipt", get_font(12), 927, 214, DIM)

# Card 3 – Invoice
illus_card(bd, 1018, 55)
# header strip
rr(bd, 1034, 100, 1148, 112, r=3, fill=(58, 100, 155))
# two product rows
product_row(bd, 1034, 120, iw=26, ih=28, row_color=ROW1, bar_x=1068, bw=68)
product_row(bd, 1034, 156, iw=26, ih=28, row_color=ROW4, bar_x=1068, bw=68)
text_cx(bd, "Invoice PDF", get_font(12), 1091, 200, DIM)

path_banner = os.path.join(OUTPUT, "banner.png")
banner.save(path_banner, "PNG", optimize=True)
print(f"Saved: {path_banner}")


# ═══════════════════════════════════════════════════════════════
#  ICON  128 × 128
# ═══════════════════════════════════════════════════════════════

IW, IH = 128, 128

# Gradient base (RGB)
icon_base = Image.new("RGB", (IW, IH))
ib = ImageDraw.Draw(icon_base)
hgradient(ib, IW, IH, DARK, MID, LIGHT)

# Rounded-square mask
mask = Image.new("L", (IW, IH), 0)
md  = ImageDraw.Draw(mask)
md.rounded_rectangle([(0, 0), (IW - 1, IH - 1)], radius=22, fill=255)

# Paste gradient onto transparent canvas
icon = Image.new("RGBA", (IW, IH), (0, 0, 0, 0))
icon.paste(icon_base, mask=mask)
ic = ImageDraw.Draw(icon)

# ── Cart icon ────────────────────────────────────────────────────
# Handle bar  (handle)
ic.line([(16, 28), (30, 28)], fill=WHITE, width=5)
# Cart body bottom rail
ic.line([(30, 28), (48, 82), (94, 82)], fill=WHITE, width=5)
# Top rail across cart
ic.line([(36, 44), (106, 44), (94, 82)], fill=WHITE, width=5)
# Left incline
ic.line([(30, 28), (36, 44)], fill=WHITE, width=5)
# Wheels
ic.ellipse([40, 88, 56, 104], fill=WHITE)
ic.ellipse([78, 88, 94, 104], fill=WHITE)

# Product image frame inside cart
rr(ic, 48, 48, 82, 76, r=5, fill=(50, 100, 170, 140), outline=WHITE, width=2)
# Mini landscape in frame (mountain + sun)
ic.polygon([(51, 73), (65, 54), (79, 73)], fill=(200, 228, 255, 180))
ic.ellipse([(71, 51), (78, 58)], fill=(255, 240, 180, 220))

path_icon = os.path.join(OUTPUT, "icon.png")
icon.save(path_icon, "PNG", optimize=True)
print(f"Saved: {path_icon}")

print("Done.")
