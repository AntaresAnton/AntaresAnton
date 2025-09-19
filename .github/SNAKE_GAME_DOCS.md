# 🐍 Snake Game Animation - Documentación

## ¿Qué hace este workflow?

Este GitHub Action genera automáticamente una animación de una serpiente "comiendo" tus contribuciones de GitHub. Es una forma divertida y visual de mostrar tu actividad en GitHub.

## 📁 Archivos creados:

### Workflows:
- `.github/workflows/snake.yml` - Workflow principal que genera la animación
- `.github/workflows/setup-snake.yml` - Workflow de configuración inicial

### Outputs generados:
- `github-contribution-grid-snake.svg` - Versión para modo claro
- `github-contribution-grid-snake-dark.svg` - Versión para modo oscuro  
- `ocean.gif` - Versión animada con colores del océano

## ⚙️ Configuración:

### 1. Habilitar GitHub Pages:
1. Ve a tu repositorio en GitHub
2. Settings > Pages
3. Source: Deploy from a branch
4. Branch: `output` / `/ (root)`
5. Save

### 2. Habilitar Workflows:
1. Ve a Actions en tu repositorio
2. Si está deshabilitado, habilítalo
3. Los workflows se ejecutarán automáticamente

### 3. Ejecutar manualmente:
1. Ve a Actions > "Generate Snake Animation"
2. Click en "Run workflow"
3. Run workflow

## 🔄 Programación automática:

- **Cada 12 horas**: Se ejecuta automáticamente
- **En cada push a main**: Se actualiza cuando haces cambios
- **Manual**: Puedes ejecutarlo cuando quieras

## 🎨 Personalización:

### Cambiar colores:
Edita el archivo `snake.yml` en la línea de `outputs`:

```yaml
outputs: |
  dist/github-contribution-grid-snake.svg
  dist/github-contribution-grid-snake-dark.svg?palette=github-dark
  dist/ocean.gif?color_snake=orange&color_dots=#bfd6f6,#8dbdff,#64a1f4,#4b91f1,#3c7dd9
```

### Opciones de color:
- `color_snake`: Color de la serpiente (orange, red, blue, green, etc.)
- `color_dots`: Colores de los puntos (contribuciones)
- `palette`: Paleta de colores (github-dark, github-light, etc.)

## 🚀 URLs de las animaciones:

Una vez que el workflow se ejecute, las animaciones estarán disponibles en:

```
https://raw.githubusercontent.com/AntaresAnton/AntaresAnton/output/github-contribution-grid-snake.svg
https://raw.githubusercontent.com/AntaresAnton/AntaresAnton/output/github-contribution-grid-snake-dark.svg
```

## 🔧 Troubleshooting:

### Si el workflow falla:
1. Verifica que GitHub Pages esté habilitado
2. Verifica que el repositorio sea público o tengas GitHub Pro
3. Revisa los logs en la pestaña Actions

### Si no aparece la animación:
1. Espera a que el workflow se ejecute (puede tomar unos minutos)
2. Verifica la URL en tu README
3. Fuerza un refresh del cache del navegador (Ctrl+F5)

## 📊 Métricas:

El workflow genera estadísticas sobre:
- Total de contribuciones del último año
- Contribuciones por día
- Racha más larga de contribuciones
- Patrones de actividad

¡Tu snake game estará listo para mostrar tu actividad de GitHub de forma súper cool! 🎮🐍