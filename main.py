import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from urllib.error import URLError, HTTPError

class ConfigError(Exception):
    """Пользовательское исключение для ошибок конфигурации"""
    pass

class DependencyVisualizer:
    """Класс для визуализации зависимостей .NET пакетов"""
    
    def __init__(self):
        """Инициализация класса DependencyVisualizer"""
        self.config = {}
        self.required_params = [
            'package_name',
            'repo_url_or_path', 
            'test_repo_mode',
            'package_version',
            'max_depth',
            'filter_substring'
        ]

    def load_config(self, config_path):
        """
        Загрузка конфигурации из JSON файла
        
        Args:
            config_path (str): Путь к файлу конфигурации
            
        Raises:
            ConfigError: Если файл не найден или имеет неверный формат
        """
        try:            
            with open(config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
                
        except FileNotFoundError:
            raise ConfigError(f"Конфигурационный файл не найден: {config_path}")
        except json.JSONDecodeError as e:
            raise ConfigError(f"Ошибка формата JSON: {e}")
        except Exception as e:
            raise ConfigError(f"Ошибка чтения файла: {e}")

    def validate_config(self):
        """
        Валидация параметров конфигурации
        
        Raises:
            ConfigError: Если параметры отсутствуют или имеют неверный тип
        """
        if not self.config:
            raise ConfigError("Конфигурация не загружена")
            
        # Проверка наличия обязательных параметров
        for param in self.required_params:
            if param not in self.config:
                raise ConfigError(f"Отсутствует обязательный параметр: {param}")
        
        # Проверка типов данных
        if not isinstance(self.config['package_name'], str):
            raise ConfigError("package_name должен быть строкой")
            
        if not isinstance(self.config['repo_url_or_path'], str):
            raise ConfigError("repo_url_or_path должен быть строкой")
            
        if not isinstance(self.config['test_repo_mode'], bool):
            raise ConfigError("test_repo_mode должен быть булевым значением")
            
        if not isinstance(self.config['package_version'], str):
            raise ConfigError("package_version должен быть строкой")
            
        if not isinstance(self.config['max_depth'], int) or self.config['max_depth'] < 0:
            raise ConfigError("max_depth должен быть неотрицательным целым числом")
            
        if not isinstance(self.config['filter_substring'], str):
            raise ConfigError("filter_substring должен быть строкой")

    def print_config(self):
        """Вывод всех параметров конфигурации в форматированном виде"""
        print("\n=== Параметры конфигурации ===")
        for key, value in self.config.items():
            print(f"{key}: {value}")
        print("==============================\n")

    def fetch_nuget_dependencies(self):
        """
        Получение прямых зависимостей из NuGet репозитория
        
        Returns:
            list: Список зависимостей в формате "пакет версия"
        """
        package_name = self.config['package_name']
        package_version = self.config['package_version']
        repo_url = self.config['repo_url_or_path']
        
        # Формируем URL для получения nuspec файла
        nuspec_url = f"{repo_url}/{package_name}/{package_version}/{package_name}.nuspec"
        
        print(f"Загрузка зависимостей для {package_name} {package_version}")
        print(f"URL: {nuspec_url}")
        
        try:
            # Загружаем nuspec файл
            with urllib.request.urlopen(nuspec_url) as response:
                nuspec_content = response.read().decode('utf-8')
                
            # Парсим XML
            root = ET.fromstring(nuspec_content)
            
            # Находим все зависимости
            namespaces = {
                'ns': 'http://schemas.microsoft.com/packaging/2013/05/nuspec.xsd'
            }
            
            dependencies = []
            
            # Ищем зависимости в разных местах nuspec
            dependency_elements = root.findall('.//ns:dependency', namespaces)
            group_elements = root.findall('.//ns:group', namespaces)
            
            for dep in dependency_elements:
                dep_id = dep.get('id')
                dep_version = dep.get('version', '')
                if dep_id:
                    dependencies.append(f"{dep_id} {dep_version}".strip())
            
            for group in group_elements:
                group_deps = group.findall('ns:dependency', namespaces)
                for dep in group_deps:
                    dep_id = dep.get('id')
                    dep_version = dep.get('version', '')
                    if dep_id:
                        dependencies.append(f"{dep_id} {dep_version}".strip())
            
            # Удаляем дубликаты
            dependencies = list(set(dependencies))
            
            print("\n=== Прямые зависимости ===")
            if dependencies:
                for dep in sorted(dependencies):
                    print(f"  - {dep}")
            else:
                print("  Зависимости не найдены")
            print("==========================\n")
            
            return dependencies
            
        except HTTPError as e:
            print(f"Ошибка HTTP при загрузке зависимостей: {e.code} {e.reason}")
            return []
        except URLError as e:
            print(f"Ошибка URL при загрузке зависимостей: {e.reason}")
            return []
        except ET.ParseError as e:
            print(f"Ошибка парсинга XML: {e}")
            return []
        except Exception as e:
            print(f"Неожиданная ошибка при получении зависимостей: {e}")
            return []

    def run(self, config_path):
        """
        Основной метод выполнения программы
        
        Args:
            config_path (str): Путь к файлу конфигурации
        """
        try:
            # Этап 1: Загрузка и валидация конфигурации
            self.load_config(config_path)
            self.validate_config()
            self.print_config()
            
            # Этап 2: Получение зависимостей (только если не тестовый режим)
            if not self.config['test_repo_mode']:
                self.fetch_nuget_dependencies()
            else:
                print("Режим тестового репозитория - пропуск загрузки зависимостей")
                        
        except ConfigError as e:
            print(f"Ошибка конфигурации: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
            sys.exit(1)

def main():
    """Точка входа в приложение"""
    if len(sys.argv) != 2 or ('--help' in sys.argv or '-h' in sys.argv):
        print("Использование: python main.py <config_file.json>")
        print("Пример: python main.py config.json")
        sys.exit(1)
    
    config_file = sys.argv[1]
    visualizer = DependencyVisualizer()
    visualizer.run(config_file)

if __name__ == "__main__":
    main()
