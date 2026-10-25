#!/usr/bin/env bash
# Installe ou met à jour GitHub Copilot CLI sur macOS via l'installateur officiel.
set -Eeuo pipefail

say() { printf '\n%s\n' "$*"; }
fail() { printf 'Erreur : %s\n' "$*" >&2; exit 1; }

[[ "$(uname -s)" == "Darwin" ]] || fail "ce script est réservé à macOS."
command -v curl >/dev/null 2>&1 || fail "curl est requis pour télécharger l'installateur officiel."
command -v bash >/dev/null 2>&1 || fail "bash est requis."

arch="$(uname -m)"
case "$arch" in
  arm64|x86_64) ;;
  *) say "Architecture détectée : $arch. L'installateur officiel déterminera si elle est prise en charge." ;;
esac

prefix="${PREFIX:-$HOME/.local}"
bin_dir="$prefix/bin"
mkdir -p "$bin_dir"

say "Installation de GitHub Copilot CLI"
say "Système : macOS ($arch)"
say "Répertoire d'installation : $bin_dir"
say "L'installateur provient de https://gh.io/copilot-install."

tmp_installer="$(mktemp -t copilot-cli-install.XXXXXX)"
trap 'rm -f "$tmp_installer"' EXIT

curl --fail --location --silent --show-error https://gh.io/copilot-install --output "$tmp_installer" \
  || fail "impossible de télécharger l'installateur officiel. Vérifie la connexion puis réessaie."

# PREFIX contrôle l'emplacement d'installation selon la documentation officielle.
PREFIX="$prefix" bash "$tmp_installer" || fail "l'installation de Copilot CLI a échoué."

# Ajoute le répertoire d'installation au PATH des prochaines sessions zsh sans doublon.
zprofile="$HOME/.zprofile"
path_line='export PATH="$HOME/.local/bin:$PATH"'
if [[ "$prefix" == "$HOME/.local" ]]; then
  touch "$zprofile"
  if ! grep -Fqx "$path_line" "$zprofile"; then
    {
      printf '\n# GitHub Copilot CLI\n'
      printf '%s\n' "$path_line"
    } >> "$zprofile"
  fi
fi

export PATH="$bin_dir:$PATH"
if ! command -v copilot >/dev/null 2>&1; then
  fail "installation terminée, mais 'copilot' n'est pas trouvé dans le PATH. Vérifie $bin_dir."
fi

say "Installation vérifiée : $(command -v copilot)"
if copilot --version; then
  :
else
  say "La commande --version n'est pas prise en charge par cette version ; l'exécutable est présent."
fi

say "Prochaine étape : lance 'copilot', puis saisis /login pour connecter ton compte GitHub."
say "Pour utiliser Copilot dans le terminal actuel : export PATH=\"$bin_dir:\$PATH\""
say "Ouvre un nouveau terminal (ou exécute 'source ~/.zprofile') pour recharger le PATH."
