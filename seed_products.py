"""
Run: python seed_products.py
Seeds 50+ realistic products across 15 categories.
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Category, Product

# ── Categories ────────────────────────────────────────────
CATS = [
    ("Mobiles",          "mobile"),
    ("Laptops",          "laptop"),
    ("Tablets",          "tablet"),
    ("Smart Watches",    "smartwatch"),
    ("Earbuds",          "earbuds"),
    ("Headphones",       "headphones"),
    ("Speakers",         "speaker"),
    ("Cameras",          "camera"),
    ("Gaming",           "gaming"),
    ("Monitors",         "monitor"),
    ("Sofas",            "sofa"),
    ("Chairs",           "chair"),
    ("Tables",           "table"),
    ("Appliances",       "appliance"),
    ("Accessories",      "accessories"),
]

cats = {}
for name, slug in CATS:
    c, _ = Category.objects.get_or_create(slug=slug, defaults={'name': name})
    cats[slug] = c
    print(f"  ✓ Category: {name}")

# ── Products ─────────────────────────────────────────────
PRODUCTS = [
    # ── MOBILES ──
    dict(productName="Samsung Galaxy S25 Ultra", category=cats["mobile"], price=134999,
         imgUrl="https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=500&q=80",
         shortDesc="200MP Camera · Snapdragon 8 Elite · 5000mAh · 45W Charging",
         description="The Galaxy S25 Ultra sets a new benchmark for mobile photography with a 200MP main sensor and built-in S Pen. Snapdragon 8 Elite chip delivers unmatched performance.",
         avgRating=4.9, discount=8, inStock=True),

    dict(productName="iPhone 16 Pro Max", category=cats["mobile"], price=159900,
         imgUrl="https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=500&q=80",
         shortDesc="A18 Pro Chip · 48MP Camera System · Titanium · 4K ProRes",
         description="iPhone 16 Pro Max with A18 Pro chip, a stunning 6.9-inch Super Retina XDR display, and an advanced camera system with 5x Telephoto.",
         avgRating=4.9, discount=5, inStock=True),

    dict(productName="OnePlus 13", category=cats["mobile"], price=69999,
         imgUrl="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&q=80",
         shortDesc="Snapdragon 8 Elite · 50MP Hasselblad · 100W SuperVOOC",
         description="OnePlus 13 powered by Snapdragon 8 Elite with Hasselblad camera system and industry-leading 100W SuperVOOC charging.",
         avgRating=4.7, discount=10, inStock=True),

    dict(productName="Google Pixel 10 Pro", category=cats["mobile"], price=109999,
         imgUrl="https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=500&q=80",
         shortDesc="Google Tensor G5 · 50MP Main · 7 years updates · AI Photography",
         description="Google Pixel 10 Pro runs on the custom Tensor G5 chip with 7 years of OS and security updates. Best-in-class computational photography.",
         avgRating=4.8, discount=6, inStock=True),

    dict(productName="Realme GT 7 Pro", category=cats["mobile"], price=44999,
         imgUrl="https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=500&q=80",
         shortDesc="Snapdragon 8 Elite · 50MP · 120W SuperVOOC · 6.78\" AMOLED",
         description="Realme GT 7 Pro brings flagship Snapdragon 8 Elite at a competitive price with 120W ultra-fast charging.",
         avgRating=4.5, discount=12, inStock=True),

    dict(productName="Xiaomi 15 Ultra", category=cats["mobile"], price=99999,
         imgUrl="https://images.unsplash.com/photo-1580910051074-3eb694886505?w=500&q=80",
         shortDesc="Leica Summilux Optics · 50MP × 3 cameras · 90W HyperCharge",
         description="Xiaomi 15 Ultra with Leica co-engineered optics across three 50MP cameras and HyperOS 2.0 for the ultimate flagship experience.",
         avgRating=4.7, discount=7, inStock=True),

    # ── LAPTOPS ──
    dict(productName="Dell XPS 15 (2025)", category=cats["laptop"], price=169999,
         imgUrl="https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=500&q=80",
         shortDesc="Intel Core Ultra 9 · 32GB · 1TB SSD · OLED 4K Touch · RTX 4070",
         description="Dell XPS 15 with an Ultra-thin design, stunning OLED display, and powerful Intel Core Ultra 9 processor for creators and professionals.",
         avgRating=4.8, discount=10, inStock=True),

    dict(productName="Apple MacBook Pro 16 M4", category=cats["laptop"], price=249900,
         imgUrl="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&q=80",
         shortDesc="M4 Pro Chip · 48GB Unified · 1TB SSD · 22-hr Battery · Liquid Retina XDR",
         description="MacBook Pro 16 with M4 Pro delivers unprecedented performance for professional workflows with up to 22 hours of battery life.",
         avgRating=4.9, discount=0, inStock=True),

    dict(productName="Lenovo Legion Pro 7i Gen 9", category=cats["laptop"], price=189999,
         imgUrl="https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500&q=80",
         shortDesc="Intel i9-14900HX · 32GB DDR5 · RTX 4080 · 240Hz Mini-LED",
         description="Lenovo Legion Pro 7i is built for elite gaming with Intel Core i9 HX, RTX 4080, and a 240Hz Mini-LED display.",
         avgRating=4.7, discount=8, inStock=True),

    dict(productName="HP Pavilion Plus 14 OLED", category=cats["laptop"], price=79999,
         imgUrl="https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=500&q=80",
         shortDesc="Intel Core Ultra 7 · 16GB · 512GB · 2.8K OLED 120Hz",
         description="HP Pavilion Plus 14 features a brilliant 2.8K OLED display with Intel Core Ultra 7 for everyday excellence.",
         avgRating=4.4, discount=15, inStock=True),

    dict(productName="ASUS ROG Zephyrus G14", category=cats["laptop"], price=149999,
         imgUrl="https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=500&q=80",
         shortDesc="AMD Ryzen AI 9 · RTX 4070 · 32GB LPDDR5X · 2.5K 165Hz OLED",
         description="ASUS ROG Zephyrus G14 — the ultimate compact gaming powerhouse with AMD Ryzen AI 9 and stunning OLED display.",
         avgRating=4.8, discount=5, inStock=True),

    # ── TABLETS ──
    dict(productName="Apple iPad Pro 13 M4", category=cats["tablet"], price=119900,
         imgUrl="https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500&q=80",
         shortDesc="M4 Chip · Ultra Retina XDR OLED · Apple Pencil Pro · 5G",
         description="iPad Pro 13 with M4 chip and tandem OLED display — the thinnest Apple product ever, designed for ultimate creative professionals.",
         avgRating=4.9, discount=0, inStock=True),

    dict(productName="Samsung Galaxy Tab S10 Ultra", category=cats["tablet"], price=109999,
         imgUrl="https://images.unsplash.com/photo-1589739900266-43b2843f4c12?w=500&q=80",
         shortDesc="Snapdragon 8 Gen 3 · 14.6\" AMOLED · S Pen · 12GB RAM",
         description="Galaxy Tab S10 Ultra with massive 14.6-inch Dynamic AMOLED 2X display and Snapdragon 8 Gen 3 for Android's best tablet experience.",
         avgRating=4.7, discount=10, inStock=True),

    dict(productName="OnePlus Pad 2", category=cats["tablet"], price=47999,
         imgUrl="https://images.unsplash.com/photo-1561154464-82e9adf32764?w=500&q=80",
         shortDesc="Snapdragon 8 Gen 3 · 12.1\" LTPO · 9510mAh · 67W SUPERVOOC",
         description="OnePlus Pad 2 is a powerhouse tablet with Snapdragon 8 Gen 3, a gorgeous 12.1-inch display, and a massive battery.",
         avgRating=4.5, discount=8, inStock=True),

    # ── SMART WATCHES ──
    dict(productName="Apple Watch Series 10", category=cats["smartwatch"], price=46900,
         imgUrl="https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500&q=80",
         shortDesc="S10 Chip · Largest display · Thinnest design · ECG · Crash Detection",
         description="Apple Watch Series 10 is Apple's most advanced watch with the largest and most power-efficient display, thinnest case, and fastest charging.",
         avgRating=4.9, discount=0, inStock=True),

    dict(productName="Samsung Galaxy Watch 8 Ultra", category=cats["smartwatch"], price=74999,
         imgUrl="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&q=80",
         shortDesc="Titanium · Advanced Health Sensors · 4G LTE · Dual-band GPS",
         description="Galaxy Watch 8 Ultra with rugged titanium design, advanced health monitoring including blood pressure and body composition.",
         avgRating=4.7, discount=5, inStock=True),

    dict(productName="Garmin Fenix 8 Sapphire", category=cats["smartwatch"], price=89999,
         imgUrl="https://images.unsplash.com/photo-1508057198894-247b23fe5ade?w=500&q=80",
         shortDesc="Sapphire lens · Multiband GPS · 29-day battery · Health Suite",
         description="Garmin Fenix 8 is the ultimate adventure smartwatch with sapphire lens, advanced GPS and up to 29 days battery life.",
         avgRating=4.8, discount=0, inStock=True),

    dict(productName="Noise ColorFit Ultra 3", category=cats["smartwatch"], price=3999,
         imgUrl="https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=500&q=80",
         shortDesc="1.96\" AMOLED · BT Calling · SpO2 · Heart Rate · 7-day Battery",
         description="Noise ColorFit Ultra 3 packs premium features at an unbeatable price — Bluetooth calling, health suite, and a stunning AMOLED display.",
         avgRating=4.2, discount=30, inStock=True),

    # ── EARBUDS ──
    dict(productName="Apple AirPods Pro 3", category=cats["earbuds"], price=26900,
         imgUrl="https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?w=500&q=80",
         shortDesc="H3 Chip · Active Noise Cancellation · Hearing Health · 36hr Total",
         description="AirPods Pro 3 with H3 chip delivers the most advanced hearing experience with clinical-grade hearing health features and adaptive audio.",
         avgRating=4.9, discount=0, inStock=True),

    dict(productName="Samsung Galaxy Buds 3 Pro", category=cats["earbuds"], price=17999,
         imgUrl="https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=500&q=80",
         shortDesc="Intelligent ANC · 360 Audio · 30hr Total · IP57 · SSC HiFi",
         description="Galaxy Buds 3 Pro with redesigned blade design, 360-degree audio, and intelligent ANC that adapts to your ear canal.",
         avgRating=4.7, discount=12, inStock=True),

    dict(productName="boAt Airdopes 800", category=cats["earbuds"], price=2999,
         imgUrl="https://images.unsplash.com/photo-1572536147248-ac59a8abfa4b?w=500&q=80",
         shortDesc="50H Playtime · ENx Tech · Beast Mode · IPX5 · 13mm Drivers",
         description="boAt Airdopes 800 with massive 50H playtime, Beast Mode for gaming, and ENx mic technology for crystal-clear calls.",
         avgRating=4.3, discount=40, inStock=True),

    dict(productName="Nothing Ear (3)", category=cats["earbuds"], price=12999,
         imgUrl="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&q=80",
         shortDesc="45dB ANC · ChatConnect AI · 42.5H Total · Transparent Design",
         description="Nothing Ear 3 — iconic transparent design with powerful 45dB ANC, ChatConnect AI for seamless switching, and premium Hi-Res audio.",
         avgRating=4.6, discount=0, inStock=True),

    dict(productName="OnePlus Buds Pro 3", category=cats["earbuds"], price=11999,
         imgUrl="https://images.unsplash.com/photo-1598371839696-5c5bb00bdc28?w=500&q=80",
         shortDesc="Dynaudio Tuning · 49dB ANC · LHDC 5.0 · 43H Total",
         description="OnePlus Buds Pro 3 co-developed with Dynaudio for premium sound, boasting 49dB industry-leading ANC and LHDC 5.0 lossless audio.",
         avgRating=4.5, discount=10, inStock=True),

    # ── HEADPHONES ──
    dict(productName="Sony WH-1000XM6", category=cats["headphones"], price=34990,
         imgUrl="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&q=80",
         shortDesc="Industry-best ANC · 40hr Battery · LDAC · Multipoint · Foldable",
         description="Sony WH-1000XM6 continues Sony's legacy of best-in-class noise cancellation with upgraded QN3 processor and improved spatial audio.",
         avgRating=4.9, discount=10, inStock=True),

    dict(productName="Bose QuietComfort 45", category=cats["headphones"], price=29900,
         imgUrl="https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=500&q=80",
         shortDesc="World-class ANC · 24hr Battery · TriPort Acoustic · USB-C",
         description="Bose QC45 headphones deliver legendary Bose noise cancellation in an ultra-comfortable design for all-day listening.",
         avgRating=4.7, discount=8, inStock=True),

    dict(productName="Sennheiser Momentum 4 Wireless", category=cats["headphones"], price=32999,
         imgUrl="https://images.unsplash.com/photo-1583394838336-acd977736f90?w=500&q=80",
         shortDesc="60HR Battery · Adaptive ANC · Hi-Res Audio · aptX Adaptive",
         description="Sennheiser Momentum 4 Wireless delivers audiophile-grade sound with an incredible 60-hour battery and adaptive noise cancellation.",
         avgRating=4.8, discount=5, inStock=True),

    # ── SPEAKERS ──
    dict(productName="JBL Charge 6", category=cats["speaker"], price=16999,
         imgUrl="https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500&q=80",
         shortDesc="IP67 Waterproof · 25hr Battery · Power Bank · PartyBoost",
         description="JBL Charge 6 with powerful JBL Pro Sound, massive 25-hour playtime, IP67 waterproof rating, and a built-in power bank.",
         avgRating=4.7, discount=10, inStock=True),

    dict(productName="Bose SoundLink Max", category=cats["speaker"], price=42900,
         imgUrl="https://images.unsplash.com/photo-1589003077984-894e133dabab?w=500&q=80",
         shortDesc="Premium 360° Sound · 20hr Battery · IP67 · USB-C · Lossless",
         description="Bose SoundLink Max delivers room-filling premium sound in a portable package with Bose's legendary audio quality.",
         avgRating=4.8, discount=0, inStock=True),

    dict(productName="Marshall Emberton III", category=cats["speaker"], price=14999,
         imgUrl="https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500&q=80",
         shortDesc="Multi-Directional Sound · 30hr Battery · IP67 · USB-C",
         description="Marshall Emberton III — authentic rock 'n' roll sound in a bold portable design with impressive 30-hour battery.",
         avgRating=4.6, discount=5, inStock=True),

    # ── CAMERAS ──
    dict(productName="Sony Alpha A7 IV", category=cats["camera"], price=249990,
         imgUrl="https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=500&q=80",
         shortDesc="33MP BSI-CMOS · 4K 60fps · 759 AF Points · Dual Card Slots",
         description="Sony A7 IV is the all-around mirrorless powerhouse with a 33MP sensor, class-leading autofocus, and 4K 60fps video.",
         avgRating=4.9, discount=0, inStock=True),

    dict(productName="Canon EOS R8", category=cats["camera"], price=149990,
         imgUrl="https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500&q=80",
         shortDesc="24.2MP Full Frame · 4K 60fps · DIGIC X · Compact Body",
         description="Canon EOS R8 brings full-frame performance in the most compact R-series body, perfect for enthusiasts and content creators.",
         avgRating=4.7, discount=5, inStock=True),

    dict(productName="GoPro HERO 13 Black", category=cats["camera"], price=44999,
         imgUrl="https://images.unsplash.com/photo-1554744512-d6c603f27c54?w=500&q=80",
         shortDesc="5.3K60 · HDR · HyperSmooth 7.0 · 60m Waterproof · 156° FOV",
         description="GoPro HERO 13 Black captures stunning 5.3K video with best-ever HyperSmooth stabilization and improved battery life.",
         avgRating=4.7, discount=8, inStock=True),

    # ── GAMING ──
    dict(productName="PlayStation 5 Slim", category=cats["gaming"], price=54990,
         imgUrl="https://images.unsplash.com/photo-1607853202273-232359e2f85e?w=500&q=80",
         shortDesc="Custom AMD GPU · 4K 120fps · SSD 825GB · DualSense · Ray Tracing",
         description="PS5 Slim — next-gen gaming with stunning 4K graphics, 120fps gameplay, lightning-fast SSD, and the revolutionary DualSense controller.",
         avgRating=4.9, discount=0, inStock=True),

    dict(productName="Xbox Series X", category=cats["gaming"], price=54990,
         imgUrl="https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=500&q=80",
         shortDesc="12 TFLOPS · 4K 120fps · 1TB NVMe · Quick Resume · Game Pass",
         description="Xbox Series X is the most powerful Xbox ever with 12 teraflops of GPU power, 4K gaming, and Xbox Game Pass integration.",
         avgRating=4.8, discount=5, inStock=True),

    dict(productName="Nintendo Switch OLED", category=cats["gaming"], price=34999,
         imgUrl="https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=500&q=80",
         shortDesc="7\" OLED Display · 64GB Storage · Handheld & TV Mode · Kickstand",
         description="Nintendo Switch OLED with a vibrant 7-inch OLED screen for stunning handheld gaming, plus a wide adjustable stand.",
         avgRating=4.8, discount=0, inStock=True),

    dict(productName="Razer DeathAdder V3 HyperSpeed", category=cats["gaming"], price=7999,
         imgUrl="https://images.unsplash.com/photo-1563297007-0686b7003af7?w=500&q=80",
         shortDesc="Razer HyperSpeed · 300hr Battery · 26K DPI · Ergonomic Design",
         description="Razer DeathAdder V3 HyperSpeed — the world's most popular gaming mouse shape, now wireless and faster than ever.",
         avgRating=4.6, discount=15, inStock=True),

    # ── MONITORS ──
    dict(productName="LG UltraGear 32GS95UE", category=cats["monitor"], price=129999,
         imgUrl="https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500&q=80",
         shortDesc="4K OLED · 240Hz · 0.03ms · G-Sync · HDR400 · 32\"",
         description="LG UltraGear 32GS95UE — the ultimate gaming monitor with a 4K OLED panel at 240Hz refresh rate for the most immersive gaming visuals.",
         avgRating=4.9, discount=5, inStock=True),

    dict(productName="Samsung Smart Monitor M8", category=cats["monitor"], price=64999,
         imgUrl="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=500&q=80",
         shortDesc="32\" 4K UHD · Smart TV Apps · Slimfit Camera · USB-C 65W · Wireless Dex",
         description="Samsung Smart Monitor M8 is the ultimate all-in-one display — smart TV, monitor, and wireless screen mirroring in one elegant package.",
         avgRating=4.7, discount=10, inStock=True),

    dict(productName="Dell UltraSharp U2725D", category=cats["monitor"], price=74999,
         imgUrl="https://images.unsplash.com/photo-1585792180666-f7347c490ee2?w=500&q=80",
         shortDesc="27\" IPS Black · QHD · 120Hz · USB-C · Thunderbolt 4 · Color Accurate",
         description="Dell UltraSharp U2725D — designed for creative professionals with IPS Black panel, Thunderbolt 4, and factory-calibrated color accuracy.",
         avgRating=4.8, discount=0, inStock=True),

    # ── SOFAS ──
    dict(productName="Wakefit Solace 3-Seater Sofa", category=cats["sofa"], price=34999,
         imgUrl="https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=500&q=80",
         shortDesc="Premium Fabric · High-Density Foam · Solid Sheesham Wood · 5yr Warranty",
         description="Wakefit Solace 3-seater sofa crafted with solid sheesham wood frame, high-density foam, and premium fabric for years of comfort.",
         avgRating=4.6, discount=20, inStock=True),

    dict(productName="Duroflex Snooze L-Shape Sofa", category=cats["sofa"], price=79999,
         imgUrl="https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?w=500&q=80",
         shortDesc="7-Seater L-Shape · Leatherette · Pull-Out Bed · Storage Ottoman",
         description="Duroflex Snooze L-shape sofa with pull-out bed — the perfect multi-functional centerpiece for modern living rooms.",
         avgRating=4.5, discount=15, inStock=True),

    dict(productName="Nilkamal Floyd Fabric Sofa", category=cats["sofa"], price=22999,
         imgUrl="https://images.unsplash.com/photo-1540574163026-643ea20ade25?w=500&q=80",
         shortDesc="3-Seater · Stain-Resistant Fabric · Wooden Legs · Easy Assembly",
         description="Nilkamal Floyd sofa with stain-resistant fabric upholstery and sturdy solid wood legs — an elegant choice for any living space.",
         avgRating=4.3, discount=18, inStock=True),

    # ── CHAIRS ──
    dict(productName="Green Soul Monster Ultimate", category=cats["chair"], price=24999,
         imgUrl="https://images.unsplash.com/photo-1541558869434-2840d308329a?w=500&q=80",
         shortDesc="3D Lumbar Support · 4D Armrests · Full-Recline · Mesh Back",
         description="Green Soul Monster Ultimate with 3D lumbar support, 4D adjustable armrests, and breathable mesh back for ultimate all-day comfort.",
         avgRating=4.8, discount=15, inStock=True),

    dict(productName="Herman Miller Aeron Chair", category=cats["chair"], price=149999,
         imgUrl="https://images.unsplash.com/photo-1505843490578-27c8f7339196?w=500&q=80",
         shortDesc="PostureFit SL · 8Z Pellicle Mesh · Tilt Limiter · 12-yr Warranty",
         description="Herman Miller Aeron — the world's most recognized office chair with PostureFit SL support and 8Z Pellicle suspension for all-day comfort.",
         avgRating=4.9, discount=0, inStock=True),

    dict(productName="Featherlite Optima Executive Chair", category=cats["chair"], price=18999,
         imgUrl="https://images.unsplash.com/photo-1506439773649-6e0eb8cfb237?w=500&q=80",
         shortDesc="High-Back · Leatherette · Synchronized Tilt · Height Adjustable",
         description="Featherlite Optima executive chair with premium leatherette upholstery and synchronized tilt mechanism for professional office settings.",
         avgRating=4.4, discount=10, inStock=True),

    # ── TABLES ──
    dict(productName="Wakefit Height-Adjustable Desk", category=cats["table"], price=29999,
         imgUrl="https://images.unsplash.com/photo-1593640408182-31c228f92e00?w=500&q=80",
         shortDesc="Electric Height Adjust · 140×70cm · Anti-Collision · 3-Preset Memory",
         description="Wakefit electric standing desk — go from sitting to standing with one touch. Anti-collision technology keeps you safe.",
         avgRating=4.7, discount=12, inStock=True),

    dict(productName="Godrej Interio Study Table", category=cats["table"], price=12999,
         imgUrl="https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=500&q=80",
         shortDesc="120×60cm · Drawer · Cable Management · Anti-Scratch Laminate",
         description="Godrej Interio study table with spacious top, integrated drawer, and cable management for a clean, organized workspace.",
         avgRating=4.3, discount=8, inStock=True),

    # ── APPLIANCES ──
    dict(productName="Samsung 253L Curd Maestro Refrigerator", category=cats["appliance"], price=37990,
         imgUrl="https://images.unsplash.com/photo-1584568694244-14fbdf83bd30?w=500&q=80",
         shortDesc="253L · Digital Inverter · 5 Star · Curd Making · 20yr Compressor",
         description="Samsung Curd Maestro with unique curd-making capability, Digital Inverter Technology, and 5-star energy rating.",
         avgRating=4.5, discount=20, inStock=True),

    dict(productName="LG 8 kg Front Load Washing Machine", category=cats["appliance"], price=54990,
         imgUrl="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500&q=80",
         shortDesc="8Kg · AI DD · Steam · ThinQ App · 1400 RPM · 5 Star",
         description="LG front-load with AI Direct Drive motor that automatically senses fabric weight and selects optimal wash motions.",
         avgRating=4.6, discount=15, inStock=True),

    dict(productName="Dyson V15 Detect Absolute", category=cats["appliance"], price=69900,
         imgUrl="https://images.unsplash.com/photo-1558618047-3c8c76b20fa9?w=500&q=80",
         shortDesc="Laser Dust Detection · HEPA · 60min Runtime · LCD Screen · 3 Tools",
         description="Dyson V15 Detect with laser technology that illuminates invisible dust. LCD screen shows live particle counts for a truly clean home.",
         avgRating=4.8, discount=5, inStock=True),

    # ── ACCESSORIES ──
    dict(productName="Anker 140W USB-C GaN Charger", category=cats["accessories"], price=5999,
         imgUrl="https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=500&q=80",
         shortDesc="140W · GaN · 3 Ports (2C+1A) · Foldable Pins · Universal",
         description="Anker 140W GaN charger — charge your MacBook Pro, iPad, and phone simultaneously from a single compact charger.",
         avgRating=4.7, discount=10, inStock=True),

    dict(productName="Logitech MX Master 3S Mouse", category=cats["accessories"], price=10995,
         imgUrl="https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500&q=80",
         shortDesc="8K DPI · MagSpeed Wheel · Quiet Click · USB-C · Multi-Device",
         description="Logitech MX Master 3S is the master of productivity with ultra-precise 8000 DPI tracking, near-silent clicks, and MagSpeed scrolling.",
         avgRating=4.8, discount=8, inStock=True),

    dict(productName="Samsung 1TB T9 Portable SSD", category=cats["accessories"], price=13999,
         imgUrl="https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=500&q=80",
         shortDesc="1TB · 2000MB/s · USB 3.2 Gen 2×2 · IP65 · 3yr Warranty",
         description="Samsung T9 portable SSD with 2000MB/s transfer speeds over USB 3.2 Gen 2×2 for blazing-fast backup and data transfer.",
         avgRating=4.7, discount=15, inStock=True),

    dict(productName="Belkin 3-in-1 MagSafe Charger", category=cats["accessories"], price=11999,
         imgUrl="https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=500&q=80",
         shortDesc="15W MagSafe · Watch · AirPods · All-in-one Stand",
         description="Belkin 3-in-1 MagSafe charger lets you charge iPhone, Apple Watch, and AirPods simultaneously in a sleek stand.",
         avgRating=4.6, discount=0, inStock=True),
]

print(f"\n🔄 Seeding {len(PRODUCTS)} products...")
created_count = 0
updated_count = 0

for p in PRODUCTS:
    obj, created = Product.objects.update_or_create(
        productName=p['productName'],
        defaults={k: v for k, v in p.items() if k != 'productName'}
    )
    if created:
        created_count += 1
        print(f"  ✅ Created: {obj.productName}")
    else:
        updated_count += 1
        print(f"  🔄 Updated: {obj.productName}")

print(f"\n🎉 Done! {created_count} created, {updated_count} updated. Total: {Product.objects.count()} products.")
