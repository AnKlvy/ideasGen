<h1>Настройка OpenAI API ключа</h1>

<p>Для использования OpenAI API в данном проекте необходимо настроить API ключ в файле <code>views.py</code>. Следуйте инструкциям ниже, чтобы вставить API ключ:</p>

<ol>
  <li>Откройте файл <code>views.py</code> в корневой директории проекта.</li>
  <li>Найдите раздел кода, где осуществляется вызов OpenAI API.</li>
  <li>Найдите переменную с названием <code>os.environ["OPENAI_API_KEY"]</code>, которая используется для хранения API ключа.</li>
  <li>Замените значение заполнителя или существующего API ключа на ваш собственный ключ OpenAI API.</li>
</ol>

<pre><code>// views.py

// OpenAI API ключ
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
openai.api_key = os.environ["OPENAI_API_KEY"]
</code></pre>


