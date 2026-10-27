# C / C++ best practices: Qt 6

- Qt 6 + CMake (`qt_add_executable`, `qt_add_qml_module`), QML for UI with C++ models (`QAbstractListModel`, `Q_PROPERTY` with `NOTIFY`, `QML_ELEMENT`), logic out of QML; parent-child ownership for `QObject`s, `connect` with the function-pointer syntax, no blocking work on the GUI thread (`QtConcurrent`, worker `QThread`).
- Accessibility (`Accessible.name`), high-DPI and layouts that resize (`ui-responsive-accessible-modular`); code signing scripts in the CI.
