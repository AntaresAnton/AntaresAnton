# ⏰ WakaTime Setup - Guía Completa

## ¿Qué es WakaTime?

WakaTime es una herramienta que trackea automáticamente el tiempo que pasas programando en diferentes proyectos, lenguajes y archivos. Es como un "fitness tracker" para desarrolladores.

## 🚀 Paso 1: Crear cuenta en WakaTime

1. Ve a [wakatime.com](https://wakatime.com/)
2. Sign up con GitHub (recomendado)
3. Completa tu perfil

## 🔧 Paso 2: Instalar extensiones/plugins

### VS Code (Principal):
1. Abre VS Code
2. Ve a Extensions (Ctrl+Shift+X)
3. Busca "WakaTime"
4. Instala la extensión oficial de WakaTime
5. Restart VS Code

### Otros IDEs que soporta WakaTime:
- **IntelliJ IDEA / WebStorm / PyCharm**
- **Sublime Text**
- **Atom**
- **Vim/Neovim**
- **Emacs**
- **Android Studio**
- **Xcode**
- **Visual Studio**

## 🔑 Paso 3: Obtener API Key

1. Ve a [wakatime.com/api-key](https://wakatime.com/api-key)
2. Copia tu API Key (se ve así: `waka_12345678-abcd-1234-5678-123456789abc`)
3. **¡GUÁRDALA SEGURA!** - No la compartas públicamente

## ⚙️ Paso 4: Configurar en VS Code

1. Después de instalar la extensión, VS Code te pedirá la API Key
2. Pega tu API Key
3. O manualmente: `Ctrl+Shift+P` → "WakaTime: API Key"

## 🔐 Paso 5: Agregar API Key a GitHub Secrets

1. Ve a tu repositorio en GitHub
2. Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `WAKATIME_API_KEY`
5. Secret: Tu API Key de WakaTime
6. Save

## 📊 Paso 6: Configurar Privacy Settings

1. Ve a [wakatime.com/settings/account](https://wakatime.com/settings/account)
2. **Display coding activity publicly**: ✅ Enable
3. **Display languages, editors, operating systems publicly**: ✅ Enable
4. **Display best day publicly**: ✅ Enable
5. Save settings

## 🎯 ¿Qué datos trackea WakaTime?

### ✅ Lo que SÍ trackea:
- **Tiempo total de código** por día/semana/mes
- **Lenguajes de programación** más usados
- **Editores/IDEs** utilizados
- **Proyectos** en los que trabajas
- **Archivos** más editados
- **Sistemas operativos**
- **Horarios** de mayor productividad

### ❌ Lo que NO trackea:
- Contenido específico del código
- Passwords o información sensible
- Solo trackea cuando estás escribiendo código activamente

## 🏆 Beneficios:

1. **Métricas precisas** de tu actividad de desarrollo
2. **Insights** sobre tus patrones de trabajo
3. **Motivación** para mantener consistencia
4. **Portfolio profesional** con datos reales
5. **Comparación** con otros developers (opcional)

## 🎨 Widgets disponibles para GitHub:

### 1. WakaTime Stats Card:
```markdown
![WakaTime Stats](https://github-readme-stats.vercel.app/api/wakatime?username=tu_username_wakatime)
```

### 2. WakaTime Weekly Stats:
```markdown
![WakaTime Weekly](https://github-readme-stats.vercel.app/api/wakatime?username=tu_username_wakatime&layout=compact)
```

### 3. WakaTime Languages:
```markdown
![WakaTime Languages](https://wakatime.com/share/@tu_username/12345678-abcd-1234-5678-123456789abc.svg)
```

## ⚡ Tips Pro:

1. **Mantén VS Code abierto** - WakaTime solo trackea cuando el editor está activo
2. **Instala en todos tus editores** - Para tracking completo
3. **Configura proyectos** - Organiza mejor tus stats
4. **Revisa tu dashboard** - Ve tus patrones semanalmente
5. **Goals** - Establece metas de código diarias

## 🔧 Troubleshooting:

### Si no aparecen stats:
1. Verifica que la API Key esté correcta
2. Asegúrate de que las privacy settings estén públicas
3. Espera al menos 24 horas para que aparezcan datos
4. Verifica que el plugin esté activo en tu editor

### Si el widget no carga:
1. Verifica tu username de WakaTime
2. Asegúrate de que tu perfil sea público
3. Verifica la URL del widget

## 🎯 Resultado esperado:

Después de 1-2 días de uso activo, verás:
- Gráficos de tu actividad diaria
- Breakdown por lenguajes
- Tiempo total de código
- Tendencias semanales/mensuales

¡WakaTime te convertirá en un developer más consciente de tu productividad! 📈✨