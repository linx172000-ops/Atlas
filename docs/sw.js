const CACHE_NAME = 'atlas-pwa-v3';
const ASSETS = [
  './',
  './index.html',
  './atlas_data.geojson',
  './manifest.json',
  './layers_output/alineaciones_construcciones.geojson',
  './layers_output/capa_estrellas_firmamento.geojson',
  'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
  'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css'
];

// Instalar: cachear todos los assets
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((c) => c.addAll(ASSETS))
  );
  self.skipWaiting();
});

// Activar: borrar caches viejos
self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Fetch: cache-first para assets propios, network-first para tiles
self.addEventListener('fetch', (e) => {
  const url = e.request.url;

  // Tiles del mapa → network first, fallback a cache
  if (url.includes('cartocdn') || url.includes('openstreetmap') || url.includes('tile')) {
    e.respondWith(
      fetch(e.request)
        .then(res => {
          const clone = res.clone();
          caches.open(CACHE_NAME).then(c => c.put(e.request, clone));
          return res;
        })
        .catch(() => caches.match(e.request))
    );
    return;
  }

  // Assets propios → cache first
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request))
  );
});
