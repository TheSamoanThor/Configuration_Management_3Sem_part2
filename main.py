import json
import sys

class ConfigError(Exception):
    pass

class DependencyVisualizer:
    def __init__(self):
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
        try:            
            with open(config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
                
        except json.JSONDecodeError as e:
            raise ConfigError(f"Ошибка формата JSON: {e}")
        except Exception as e:
            raise ConfigError(f"Ошибка чтения файла: {e}")

    def validate_config(self):
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
        print("\n=== Параметры конфигурации ===")
        for key, value in self.config.items():
            print(f"{key}: {value}")
        print("==============================\n")

    def run(self, config_path):
        try:
            # Загрузка конфигурации
            self.load_config(config_path)
            
            # Валидация параметров
            self.validate_config()
            
            # Вывод параметров
            self.print_config()
                        
        except ConfigError as e:
            print(f"Ошибка конфигурации: {e}")
            sys.exit(1)
        except Exception as e: # обработка всех других ошибок, потом их вывод
            print(f"Неожиданная ошибка: {e}")
            sys.exit(1)

def main():
    if len(sys.argv) != 2 or ('--help' in sys.argv or '--h' in sys.argv):
        print("Использование: python dependency_visualizer.py <config_file.json>")
        sys.exit(1)
    
    config_file = sys.argv[1] # 3-ье слово в строке аргументов будет
    visualizer = DependencyVisualizer()
    visualizer.run(config_file)

if __name__ == "__main__":
    main()
