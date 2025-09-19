# ✅ WakaTime Setup Checklist

## 🚀 Quick Setup Steps:

### 1. Cuenta y extensión:
- [ ] Crear cuenta en [wakatime.com](https://wakatime.com)
- [ ] Instalar extensión de WakaTime en VS Code
- [ ] Configurar API Key en VS Code

### 2. GitHub Configuration:
- [ ] Ir a GitHub Repository → Settings → Secrets and variables → Actions
- [ ] Crear nuevo secret: `WAKATIME_API_KEY`
- [ ] Pegar tu API Key de WakaTime

### 3. Privacy Settings en WakaTime:
- [ ] Ir a [wakatime.com/settings/account](https://wakatime.com/settings/account)
- [ ] ✅ Display coding activity publicly
- [ ] ✅ Display languages, editors, operating systems publicly
- [ ] ✅ Display best day publicly
- [ ] Save settings

### 4. Activar el workflow:
- [ ] Commit y push los archivos nuevos
- [ ] Ir a Actions → "WakaTime Stats"
- [ ] Run workflow manualmente la primera vez

## 📁 Archivos creados:

- `.github/workflows/wakatime.yml` - Workflow automático
- `.github/WAKATIME_SETUP.md` - Documentación completa
- `.github/WAKATIME_CHECKLIST.md` - Este checklist
- `README.md` - Actualizado con sección WakaTime

## 🎯 Resultado esperado:

Después de 24-48 horas de usar VS Code con WakaTime:

```
⏰ Esta semana dediqué mi tiempo a:

💬 Lenguajes de programación: 
Python       ████████████████████████▓   95.2 % 
JavaScript   █▓░░░░░░░░░░░░░░░░░░░░░░░   3.8 % 
TypeScript   ▒░░░░░░░░░░░░░░░░░░░░░░░░   1.0 % 

🔥 Editores: 
VS Code      ████████████████████████▓   100.0 % 

💻 Sistema Operativo: 
Windows      ████████████████████████▓   100.0 % 
```

## 🎸 Cool tip:
¡Perfecto para mostrar que eres un developer activo mientras practicas guitarra en los breaks! 🤘

## 🔧 Troubleshooting rápido:

**Si no aparecen datos:**
1. Verifica que la extensión esté activa (icono en la barra de estado)
2. Asegúrate de que estés escribiendo código activamente
3. Verifica que las privacy settings estén públicas
4. Espera 24 horas para datos completos

**Si el workflow falla:**
1. Verifica que el secret `WAKATIME_API_KEY` esté configurado
2. Verifica que tu API Key sea correcta
3. Asegúrate de que tu perfil de WakaTime sea público

¡Listo para trackear tu tiempo de código como un pro! ⏰🚀