# Platform design guidelines (load only the platform concerned): android

## Android: Material 3 and Material 3 Expressive

- Dynamic color and tonal palettes (HCT), roles `primary` / `on-primary`, surface containers, shape scale; type scale roles.
- Window size classes (compact, medium, expanded) with navigation bar → rail → drawer; edge-to-edge with insets; predictive back.
- Components: top app bar, FAB, bottom sheet, snackbar, dialogs, chips, cards, segmented buttons, search bar. Expressive adds
  spring-based motion, shape morphing, emphasized type and color, and new components: use at the "excellent" level, not everywhere.
- Touch targets 48 dp; Compose component names help `front`.
