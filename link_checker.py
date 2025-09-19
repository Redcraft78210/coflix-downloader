import requests

def get_valid_links(base_url: str, max_attempts: int = 100):
    session = requests.Session()
    valid_links = []

    for i in range(1, max_attempts + 1):
        url = base_url.format(i)
        try:
            response = session.get(url, timeout=5)
            if response.status_code == 404:
#                print(f"❌ Fin détectée : {url} est introuvable (404)")
                break
            else:
#                print(f"✅ {url} existe (status {response.status_code})")
                valid_links.append(url)
        except requests.RequestException as e:
            print(f"⚠️ Erreur réseau pour {url} : {e}")
            break

    return valid_links


if __name__ == "__main__":
    base_url = "https://coflix.tel/episode/mercredi-2x{}"
    links = get_valid_links(base_url)
    print("\nLiens valides trouvés :")
    print(links)
