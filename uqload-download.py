#!/usr/bin/env python3

import os
import subprocess
import argparse
from link_checker import get_valid_links
from clicker import get_params_and_launch

def download_uqload_videos(urls, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)

    for video_url in urls:
        try:
            cmd = ["uqload-dl", "-u", video_url, "-o", output_dir, "-y"]
            print(f"⬇️  Téléchargement de {video_url} dans {output_dir}...")
            subprocess.run(cmd, check=True)
            print("✅ Téléchargement terminé")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors du téléchargement de {video_url} : {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Script pour extraire les liens Uqload depuis CoFlix et les télécharger avec uqload-dl."
    )
    parser.add_argument(
        "-b", "--base_url",
        type=str,
        required=True,
        help="URL de base des épisodes avec {} pour le numéro de l'épisode (ex: 'https://coflix.tel/episode/mercredi-2x{}')."
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="downloads",
        help="Dossier où seront téléchargées les vidéos."
    )

    args = parser.parse_args()

    # Vérifications simples
    if "{}" not in args.base_url:
        print("❌ Erreur : base_url doit contenir '{}' pour le numéro de l'épisode")
        return

    print(f"🔗 Extraction des liens Uqload depuis : {args.base_url}")
    final_urls = get_params_and_launch(args.base_url)

    if final_urls:
        download_uqload_videos(final_urls, args.output)
    else:
        print("❌ Aucun lien Uqload trouvé sur les épisodes")

if __name__ == "__main__":
    main()

