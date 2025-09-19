# 🎬 Coflix Downloader

🚀 Un outil simple en **Python** pour extraire automatiquement les liens **Uqload** depuis **Coflix** et télécharger tous les épisodes d’une saison via `uqload-dl`.


---

## ✨ Fonctionnalités

* 📥 Téléchargement automatique de tous les épisodes d’une saison
* 🔗 Extraction des liens **Uqload** directement depuis Coflix
* 🗂️ Organisation des vidéos dans un dossier choisi
* ✅ Gestion basique des erreurs lors du téléchargement

---

## 📦 Installation

Cloner le dépôt et installer les dépendances :

```bash
git clone https://github.com/Redcraft78210/coflix-downloader.git
cd coflix-downloader
```

⚠️ Assurez-vous aussi que l’outil **[uqload-dl](https://github.com/Sorrow446/uqload-dl)** est installé sur votre système et accessible dans le `PATH`.

---

## 🧭 Utilisation

Lancer le script principal avec une URL de base :

```bash
python main.py -b "https://urldecoflix/episode/mercredi-2x{}" -o "./mes_episodes"
```

### Arguments disponibles

* `-b`, `--base_url` (**obligatoire**) : modèle de l’URL des épisodes, doit contenir `{}` pour le numéro de l’épisode

  * ex: `"https://urldecoflix/episode/mercredi-2x{}"`
* `-o`, `--output` : dossier de sortie des vidéos (par défaut : `downloads`)

---

## 🔐 Respect de la légalité

Cet outil est uniquement destiné au téléchargement de contenu **libre de droits** ou pour lequel vous disposez d’une autorisation explicite.
**N’utilisez pas ce projet pour télécharger du contenu protégé sans licence.**

---

## 🧩 Structure du projet

```
.
├── main.py           # script principal (CLI)
├── link_checker.py   # utilitaire pour valider/extraire les liens
├── clicker.py        # automatisation de la navigation/extraction
├── requirements.txt  # dépendances Python
└── README.md
```

---

## 🛠️ Contribution

Les contributions sont les bienvenues ! 🙌

1. Fork le repo
2. Crée une branche `feature/ma-fonctionnalite`
3. Ajoute des tests + mise à jour de la doc
4. Ouvre une Pull Request

---

## ⚠️ Disclaimer

L’auteur décline toute responsabilité en cas d’usage illicite.
Utilisez cet outil **uniquement pour du contenu légal**.

---
