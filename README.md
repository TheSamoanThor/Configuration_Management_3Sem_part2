# Dependency Visualizer - .NET NuGet Package Analyzer

<hr>

<h2>Краткое описание</h2>

<p>Данный проект представляет собой инструмент визуализации графа зависимостей для менеджера пакетов .NET (NuGet). На текущем этапе реализована функциональность для работы с конфигурационными файлами и получения информации о прямых зависимостях пакетов из NuGet репозитория.</p>

<p>Программа читает настройки из JSON-файла, проверяет их корректность, выводит все параметры и получает зависимости указанного пакета через NuGet API. Это второй этап разработки полноценного инструмента анализа зависимостей пакетов.</p>

<hr>

<h2>Методы класса DependencyVisualizer</h2>

<ol>
<li>__init__</li>
<li>load_config</li>
<li>validate_config</li>
<li>print_config</li>
<li>fetch_nuget_dependencies</li>
<li>run</li>
</ol>

<hr>

<h3>__init__</h3>

<p>Конструктор класса, инициализирует пустой словарь для конфигурации и задает список обязательных параметров.</p>

<h3>load_config</h3>

<p>Загружает конфигурацию из JSON файла. Проверяет существование файла и корректность формата JSON.</p>

<h3>validate_config</h3>

<p>Проверяет наличие всех обязательных параметров в конфигурации и корректность их типов данных.</p>

<h3>print_config</h3>

<p>Выводит все параметры конфигурации в формате "ключ: значение" с форматированием.</p>

<h3>fetch_nuget_dependencies</h3>

<p>Получает прямые зависимости .NET пакета из NuGet репозитория. Формирует URL для доступа к .nuspec файлу, загружает и парсит XML для извлечения информации о зависимостях.</p>

<h3>run</h3>

<p>Основной метод выполнения этапа. Координирует загрузку, валидацию конфигурации, получение зависимостей и обработку ошибок.</p>

<hr>

<h2>Дополнительные классы и функции</h2>

<ol>
<li>ConfigError</li>
<li>main</li>
</ol>

<hr>

<h3>ConfigError</h3>

<p>Пользовательский класс исключения для обработки ошибок конфигурации. Используется для генерации понятных сообщений об ошибках.</p>

<h3>main</h3>

<p>Точка входа в приложение. Обрабатывает аргументы командной строки, создает экземпляр DependencyVisualizer и запускает основной процесс.</p>

<hr>

<h2>Обязательные параметры конфигурации</h2>

<ul>
<li>package_name - имя анализируемого пакета (строка)</li>
<li>repo_url_or_path - URL репозитория или путь к файлу тестового репозитория (строка)</li>
<li>test_repo_mode - режим работы с тестовым репозиторием (логическое значение)</li>
<li>package_version - версия пакета (строка)</li>
<li>max_depth - максимальная глубина анализа зависимостей (целое неотрицательное число)</li>
<li>filter_substring - подстрока для фильтрации пакетов (строка)</li>
</ul>

<hr>

<h2>Использование</h2>

<p>Для запуска программы выполните команду:</p>

<pre><code>python main.py config.json</code></pre>

<p>Где config.json - файл с конфигурацией в формате JSON.</p>

<p>Пример содержимого config.json:</p>

<pre><code>{
    "package_name": "Newtonsoft.Json",
    "repo_url_or_path": "https://api.nuget.org/v3-flatcontainer",
    "test_repo_mode": false,
    "package_version": "13.0.3",
    "max_depth": 3,
    "filter_substring": ""
}</code></pre>

<h3>Примеры вывода:</h3>

<pre><code>=== Параметры конфигурации ===
package_name: Newtonsoft.Json
repo_url_or_path: https://api.nuget.org/v3-flatcontainer
test_repo_mode: false
package_version: 13.0.3
max_depth: 3
filter_substring: 
==============================

Загрузка зависимостей для Newtonsoft.Json 13.0.3
URL: https://api.nuget.org/v3-flatcontainer/Newtonsoft.Json/13.0.3/Newtonsoft.Json.nuspec

=== Прямые зависимости ===
  - (зависимости не найдены или пакет не имеет зависимостей)
==========================</code></pre>

<hr>

<h2>Обработка ошибок</h2>

<p>Программа обрабатывает следующие типы ошибок:</p>

<ul>
<li>Отсутствие конфигурационного файла</li>
<li>Некорректный формат JSON</li>
<li>Отсутствие обязательных параметров</li>
<li>Некорректные типы данных параметров</li>
<li>Ошибки сети при загрузке зависимостей</li>
<li>Ошибки парсинга XML</li>
<li>Другие неожиданные ошибки</li>
</ul>

<hr>

<h2>Тестирование</h2>

<p>Для тестирования используйте различные конфигурационные файлы:</p>

<pre><code>python main.py config_ef.json
python main.py config_automapper.json
python main.py config_nonexistent.json</code></pre>

<p>Примеры конфигурационных файлов для тестирования различных сценариев:</p>

<ul>
<li>config_ef.json - Microsoft.EntityFrameworkCore (сложные зависимости)</li>
<li>config_automapper.json - AutoMapper (умеренные зависимости)</li>
<li>config_newtonsoft.json - Newtonsoft.Json (минимальные зависимости)</li>
<li>config_nonexistent.json - Несуществующий пакет (проверка ошибок)</li>
</ul>

<hr>

<h2>Short description</h2>

<p>This project is a dependency graph visualization tool for .NET NuGet package manager. The current stage implements functionality for working with configuration files and retrieving direct dependency information from NuGet repository.</p>

<p>The program reads settings from a JSON file, checks their correctness, outputs all parameters and retrieves dependencies of the specified package through NuGet API. This is the second stage of developing a full-fledged package dependency analysis tool.</p>

<hr>

<h2>Methods of the DependencyVisualizer class</h2>

<ol>
<li>__init__</li>
<li>load_config</li>
<li>validate_config</li>
<li>print_config</li>
<li>fetch_nuget_dependencies</li>
<li>run</li>
</ol>

<hr>

<h3>__init__</h3>

<p>Class constructor, initializes an empty dictionary for configuration and sets a list of required parameters.</p>

<h3>load_config</h3>

<p>Loads configuration from a JSON file. Checks for the existence of the file and the correctness of the JSON format.</p>

<h3>validate_config</h3>

<p>Checks for the presence of all required parameters in the configuration and the correctness of their data types.</p>

<h3>print_config</h3>

<p>Outputs all configuration parameters in "key: value" format with formatting.</p>

<h3>fetch_nuget_dependencies</h3>

<p>Retrieves direct dependencies of .NET package from NuGet repository. Forms URL to access .nuspec file, downloads and parses XML to extract dependency information.</p>

<h3>run</h3>

<p>The main method of the stage execution. Coordinates configuration loading, validation, dependency retrieval and error handling.</p>

<hr>

<h2>Additional classes and functions</h2>

<ol>
<li>ConfigError</li>
<li>main</li>
</ol>

<hr>

<h3>ConfigError</h3>

<p>A custom exception class for handling configuration errors. Used to generate clear error messages.</p>

<h3>main</h3>

<p>The entry point to the application. Handles command line arguments, creates an instance of DependencyVisualizer and starts the main process.</p>

<hr>

<h2>Required configuration parameters</h2>

<ul>
<li>package_name - name of the analyzed package (string)</li>
<li>repo_url_or_path - repository URL or path to the test repository file (string)</li>
<li>test_repo_mode - test repository mode (boolean)</li>
<li>package_version - package version (string)</li>
<li>max_depth - maximum dependency analysis depth (non-negative integer)</li>
<li>filter_substring - substring for filtering packages (string)</li>
</ul>

<hr>

<h2>Usage</h2>

<p>To run the program, execute the command:</p>

<pre><code>python main.py config.json</code></pre>

<p>Where config.json is a configuration file in JSON format.</p>

<p>Example of config.json content:</p>

<pre><code>{
    "package_name": "Newtonsoft.Json",
    "repo_url_or_path": "https://api.nuget.org/v3-flatcontainer",
    "test_repo_mode": false,
    "package_version": "13.0.3",
    "max_depth": 3,
    "filter_substring": ""
}</code></pre>

<hr>

<h2>Error handling</h2>

<p>The program handles the following types of errors:</p>

<ul>
<li>Missing configuration file</li>
<li>Invalid JSON format</li>
<li>Missing required parameters</li>
<li>Incorrect parameter data types</li>
<li>Network errors when loading dependencies</li>
<li>XML parsing errors</li>
<li>Other unexpected errors</li>
</ul>
