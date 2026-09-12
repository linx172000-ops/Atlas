import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ANDROID_ASSETS_DIR = os.path.join(BASE_DIR, 'android', 'app', 'src', 'main', 'assets', 'www')

def sync_assets():
    print(f'Sincronizando archivos a {ANDROID_ASSETS_DIR}...')
    os.makedirs(ANDROID_ASSETS_DIR, exist_ok=True)
    
    src_html = os.path.join(BASE_DIR, 'index.html')
    shutil.copy2(src_html, os.path.join(ANDROID_ASSETS_DIR, 'index.html'))
    print('  -> index.html copiado')
    
    src_geojson = os.path.join(BASE_DIR, 'atlas_data.geojson')
    shutil.copy2(src_geojson, os.path.join(ANDROID_ASSETS_DIR, 'atlas_data.geojson'))
    print('  -> atlas_data.geojson copiado')
    
    src_assets = os.path.join(BASE_DIR, 'assets')
    dst_assets = os.path.join(ANDROID_ASSETS_DIR, 'assets')
    if os.path.exists(dst_assets):
        shutil.rmtree(dst_assets)
    shutil.copytree(src_assets, dst_assets)
    print('  -> assets/ copiado (Leaflet local + mapa vectorial Europa)')
    
    src_report = os.path.join(BASE_DIR, 'informe_hallazgos_ia.md')
    if os.path.exists(src_report):
        shutil.copy2(src_report, os.path.join(ANDROID_ASSETS_DIR, 'informe_hallazgos_ia.md'))
        print('  -> informe_hallazgos_ia.md copiado')
        
    print('Sincronización completada con éxito.')

if __name__ == '__main__':
    sync_assets()
