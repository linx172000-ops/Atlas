# Atlas del Paisaje Histórico y Líneas Ley

Mapa interactivo arqueológico y geomántico de la Península Ibérica y Europa Occidental.

## Ver Mapa en Vivo

🗺️ **[https://linx172000-ops.github.io/atlas/](https://linx172000-ops.github.io/atlas/)**

## Qué contiene el mapa

- **292 Monumentos Megalíticos** — Dólmenes, Antas, Menhires y Cromlechs (4800–1800 a.C.)
- **388 Construcciones Medievales** — Monasterios, iglesias y enclaves Templarios (s.IX–XIV)
- **2020 Nodos Geológicos y Tectónicos** — Fallas, acuíferos, picos y vórtices naturales
- **5937 Líneas Ley Calculadas** — Red telúrica generada por algoritmo geodésico-orgánico
- **Rutas Históricas** — Camino de Santiago, Vías Romanas, Vía de la Plata
- **Líneas Ley Documentadas** — Eje de San Miguel, Eje Jacobeo, Eje Megalítico Atlántico

## Características Técnicas

- 100% estático — funciona sin backend ni base de datos
- Timeline interactivo: 4500 a.C. → 1250 d.C.
- Filtrado por capas (megalitos, geología, ley lines, medieval, hidrología, arqueoastronomía)
- PWA — instalable en móvil, funciona offline tras primera visita
- Análisis arqueoastronómico: alineaciones solsticiales, lunisticiales y estelares por precesión

## Datos

Generados y compilados mediante:
- Catálogos geofísicos de vórtices tectónicos (V-01 a V-88)
- IA local (Ollama / Qwen) para extracción de nodos naturales por país
- Algoritmo de Árbol de Expansión Mínima (Kruskal MST) para red de líneas ley
- Análisis archaeoastronómico con corrección por precesión del eje terrestre
