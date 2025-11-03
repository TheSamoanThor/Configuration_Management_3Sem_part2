# Configuration_Management_3Sem_part2

<hr>

<h2>Краткое описание</h2>

<p>Данный проект представляет собой инструмент визуализации графа зависимостей для менеджера пакетов. На текущем этапе реализована базовая функциональность для работы с конфигурационными файлами.</p>

<p>Программа читает настройки из JSON-файла, проверяет их корректность и выводит все параметры в удобном формате. Это первый этап разработки полноценного инструмента анализа зависимостей пакетов.</p>

<p>Для работы программы необходим конфигурационный файл в формате JSON, содержащий все обязательные параметры. Программа самостоятельно проверяет наличие файла, его формат и корректность всех параметров.</p>

<hr>

<h2>Методы класса DependencyVisualizer</h2>

<ol>
<li>__init__</li>
<li>load_config</li>
<li>validate_config</li>
<li>print_config</li>
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

<h3>run</h3>

<p>Основной метод выполнения этапа. Координирует загрузку, валидацию и вывод конфигурации, а также обрабатывает возможные ошибки.</p>

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








<hr>

<h2>Brief Description</h2>

<p>This project is a dependency graph visualization tool for a package manager. At this stage, basic functionality for working with configuration files has been implemented.</p>

<p>The program reads settings from a JSON file, checks their correctness, and displays all parameters in a convenient format. This is the first stage of developing a full-fledged package dependency analysis tool.</p>

<p>The program requires a JSON configuration file containing all required parameters. The program automatically checks the file's existence, format, and the correctness of all parameters.</p>

<hr>

<h2>DependencyVisualizer Class Methods</h2>

<ol>
<li>__init__</li>
<li>load_config</li>
<li>validate_config</li>
<li>print_config</li>
<li>run</li>
</ol>

<hr>

<h3>__init__</h3>

<p>Class constructor. Initializes an empty configuration dictionary and specifies a list of required parameters.</p>

<h3>load_config</h3>

<p>Loads a configuration from a JSON file. Validates the file's existence and valid JSON format.</p>

<h3>validate_config</h3>

<p>Verifies the presence of all required parameters in the configuration and the correct data types.</p>

<h3>print_config</h3>

<p>Prints all configuration parameters in key:value format with formatting.</p>

<h3>run</h3>

<p>The main method for executing the step. Coordinates loading, validation, and output of the configuration, and handles possible errors.</p>

<hr>

<h2>Additional Classes and Functions</h2>

<ol>
<li>ConfigError</li>
<li>main</li>
</ol>

<hr>

<h3>ConfigError</h3>

<p>Custom exception class for handling configuration errors. Used to generate user-friendly error messages.</p>

<h3>main</h3>

<p>The entry point to the application. Processes command-line arguments, creates a DependencyVisualizer instance, and starts the main process.</p>

<hr>

<h2>Required Configuration Parameters</h2>

<ul>
<li>package_name - name of the package to be analyzed (string)</li>
<li>repo_url_or_path - repository URL or path to the test repository file (string)</li>
<li>test_repo_mode - test repository mode (boolean)</li>
<li>package_version - package version (string)</li>
<li>max_depth - maximum dependency analysis depth (non-negative integer)</li>
<li>filter_substring - substring for filtering packages (string)</li>
</ul>

<hr>

<h2>Usage</h2>

<p>To run the program, run the following command:</p>
