import os
import re
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from link_checker import get_valid_links

def save_html(driver, url, output_dir="html_outputs", suffix="fail"):
    os.makedirs(output_dir, exist_ok=True)
    safe_name = url.replace("https://", "").replace("/", "_")
    filename = os.path.join(output_dir, f"{safe_name}_{suffix}.html")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(driver.page_source)

def extract_uqload_links(url: str, output_dir="html_outputs", headless=True):
    """
    Ouvre l'URL donnée, cherche les <li> contenant un span 'uqload vid',
    récupère l'attribut onclick encodé en Base64 et retourne la liste des URLs décodées.
    """
    options = Options()
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    decoded_urls = []

    try:
        driver.get(url)
        save_html(driver, url, output_dir, "initial")

        try:
            player_div = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "player-episode"))
            )
        except TimeoutException:
            save_html(driver, url, output_dir, "no_player_episode")
            return decoded_urls

        try:
            iframe = player_div.find_element(By.TAG_NAME, "iframe")
            driver.get(iframe.get_attribute("src"))
            save_html(driver, url, output_dir, "iframe_loaded")

            # Chercher tous les spans "uqload vid"
            try:
                spans = driver.find_elements(
                    By.XPATH,
                    "//span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'uqload vid')]"
                )
                for span in spans:
                    try:
                        li_parent = span.find_element(By.XPATH, "ancestor::li[1]")
                        onclick_value = li_parent.get_attribute("onclick")
                        match = re.search(r"showVideo\('([^']+)'", onclick_value)
                        if match:
                            base64_url = match.group(1)
                            decoded_url = base64.b64decode(base64_url).decode("utf-8")
                            decoded_urls.append(decoded_url)
                        else:
                            save_html(driver, url, output_dir, "no_base64_found")
                    except Exception:
                        save_html(driver, url, output_dir, "li_click_fail")
            except (TimeoutException, NoSuchElementException):
                save_html(driver, url, output_dir, "span_not_found")

        except Exception:
            save_html(driver, url, output_dir, "no_iframe_in_player")

    except Exception:
        save_html(driver, url, output_dir, "general_error")

    finally:
        driver.quit()

    return decoded_urls

def get_params_and_launch(base_url: str):
    """
    Récupère tous les liens valides d'épisodes, extrait les URLs Uqload et les retourne.
    """
    print("🔗 Récupération des liens valides...")
    links = get_valid_links(base_url)
    print(f"✅ {len(links)} liens valides trouvés")

    all_urls = []

    for link in links:
        urls = extract_uqload_links(link)
        if urls:
            print(f"{link} -> {urls}")
            all_urls.extend(urls)  # Ajouter toutes les URLs à la liste finale
        else:
            print(f"{link} -> Aucun lien trouvé")

    return all_urls


if __name__ == "__main__":
    base_url = "https://coflix.tel/episode/mercredi-2x{}"
    final_urls = get_params_and_launch(base_url)
    print("✅ Toutes les URLs Uqload extraites :")
    print(final_urls)

