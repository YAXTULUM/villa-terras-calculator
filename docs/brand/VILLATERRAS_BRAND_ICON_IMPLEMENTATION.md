# Administrative Record — VillaTerras Brand Icon Implementation

Project Repository: YAXTULUM/villa-terras-calculator
Brand Authority: VillaTerras logo-only cube icon
Canonical Source Repository: YAXTULUM/VillaTerras2.0
Canonical Source Path: apps/VillaTerrasBrand/
Installer Source Path: scripts/install-villaterras-brand-icons.sh

## Implementation Directive

This project adopts the VillaTerras logo-only cube icon as the governed brand mark for favicon, app icon, folder icon, dashboard badge, documentation identity, and future module-specific visual identity.

## Required Integration Targets

```text
assets/brand/favicon.ico
assets/brand/villaterras-icon-32x32.png
assets/brand/villaterras-icon-64x64.png
assets/brand/villaterras-icon-180x180.png
assets/brand/villaterras-icon-192x192.png
assets/brand/villaterras-icon-512x512.png
assets/brand/site.webmanifest
```

## Usage Rules

```text
Do not add VillaTerras.com text inside the icon.
Do not use a visible checkerboard background.
Do not replace the cube with unrelated art.
Use transparent-background icon files where possible.
Use the canonical icon pack from VillaTerras2.0 when syncing assets.
```

## Project-Level Status

```json
{
  "repository_saved_verified": true,
  "icon_standard_record_created": true,
  "binary_icon_assets_verified_in_this_repo": false,
  "deployment_verified": false,
  "runtime_verified": false
}
```

## Next Action

Run or adapt the canonical installer from `YAXTULUM/VillaTerras2.0/scripts/install-villaterras-brand-icons.sh`, then verify actual PNG/ICO files exist in the project runtime asset path.
