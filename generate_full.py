import yaml
import os

class NoTagYAMLLoader(yaml.SafeLoader):
    """Ignora tags YAML personalizadas desconhecidas ao carregar o arquivo."""
    def construct_undefined(self, node):
        return None

NoTagYAMLLoader.add_constructor(None, NoTagYAMLLoader.construct_undefined)

def load_mkdocs_yaml(file_path):
    """Carrega e retorna o conteúdo do arquivo mkdocs.yml ignorando tags customizadas."""
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.load(file, Loader=NoTagYAMLLoader)

def extract_nav_structure(nav_section):
    """Extrai os caminhos dos arquivos Markdown da estrutura 'nav'."""
    md_files = []

    def traverse_nav(nav):
        """Função recursiva para percorrer a estrutura de navegação."""
        if isinstance(nav, list):
            for item in nav:
                traverse_nav(item)
        elif isinstance(nav, dict):
            for key, value in nav.items():
                if isinstance(value, str) and value.endswith(".md"):
                    md_files.append((key, value))
                elif isinstance(value, list):
                    traverse_nav(value)

    traverse_nav(nav_section)
    return md_files

def merge_markdown_files(md_files, base_path, output_file):
    """Lê e combina os conteúdos dos arquivos Markdown na ordem correta."""
    with open(output_file, "w", encoding="utf-8") as out_file:
        for title, md_path in md_files:
            md_full_path = os.path.join(base_path, md_path)
            if os.path.exists(md_full_path):
                out_file.write(f"# {title}\n\n")  # Adiciona o título antes do conteúdo
                with open(md_full_path, "r", encoding="utf-8") as md_file:
                    out_file.write(md_file.read())
                out_file.write("\n\n---\n\n")  # Adiciona uma separação entre arquivos
            else:
                print(f"Aviso: Arquivo '{md_full_path}' não encontrado na pasta 'docs/' e será ignorado.")

def main():
    mkdocs_file = "mkdocs.yml"  # Caminho do arquivo mkdocs.yml
    base_dir = "docs"  # Agora busca os arquivos dentro de 'docs/'
    output_file = "documentacao_completa.md"  # Arquivo de saída consolidado

    # Carregar mkdocs.yml
    mkdocs_data = load_mkdocs_yaml(mkdocs_file)

    # Verificar se 'nav' está presente no mkdocs.yml
    if "nav" not in mkdocs_data:
        print("Erro: A estrutura 'nav' não foi encontrada no mkdocs.yml")
        return
    
    # Extrair a estrutura de navegação
    md_files = extract_nav_structure(mkdocs_data["nav"])

    # Mesclar e salvar os arquivos Markdown
    merge_markdown_files(md_files, base_dir, output_file)
    print(f"Documentação consolidada salva em '{output_file}'.")

if __name__ == "__main__":
    main()
